import time
from datetime import date
from hashlib import sha256
from requests_ratelimiter import LimiterSession
from client.models.equipment import EquipmentResult
from client.models.sites import SitesResult
from client.results import PaginatedAPI
from client.utils import UrlBuilder

valid_countries = ("USA", "CAN")
        

class SystemApiClient:

    def __init__(self, org_name: str, country: str, api_key: str, secret: str) -> None:
        self.org_name = org_name
        self.country = country
        self.api_key = api_key
        self.secret = secret
        self.default_page_size = 50
        
        if not self._check_country(self.country):
            raise ValueError(f"Country must be one of {valid_countries[0]} or {valid_countries[1]}")
        
        self.session = LimiterSession(per_second=2)
        self.url = UrlBuilder(self.org_name, self.country)

    def _check_country(self, country_name):
        return country_name in valid_countries
    
    def _extract_args(self, arg_dict):
        request_args = arg_dict.copy()
        request_args.pop("self")
        request_args = { k:v for (k,v) in request_args.items() if v is not None }
        return request_args
    
    def _generate_signature(self):
        value = self.api_key + self.secret + str(int(time.time()))
        return sha256(value.encode()).hexdigest()
    
    # Default params will consist of [non empty api function parameters] + api_key + sig
    def _create_default_params(self, arg_dict):
        request_params = self._extract_args(arg_dict)
        request_params['api_key'] = self.api_key
        request_params['sig'] = self._generate_signature()
        return request_params

    def get_sites(self):
        params = self._create_default_params(locals())
        endpoint = self.url.get_endpoint('sites')  
        return PaginatedAPI(self.session, endpoint, params, SitesResult).request()

    def get_equipment( 
        self,
        equipment_id: int = None,
        center_ids: str = None,
        bookable_or_lendable: int = None,
        modified_date_from: date = None,
        modified_date_to: date = None,
        show_on_member_app: bool = None,
        open_block_date_from: date = None,
    ):
        '''
        ** Note: At least one of the following parameters must be provided: 
        'equipment_id', 'center_ids', 'modified_date_from' and 'modified_date_to'.

        Has Params:      True
        Is Paginated:    True
        Allows Sorting:  False

        Retrieves an object representing the request to the Active Net Get Equipment API Endpoint

        param: equipment_id | string
            - The ID of the equipment item
        
        param: center_ids | string
            - You can specify up to 5 center IDs, with each center ID separated by a comma.

        param: bookable_or_lendable | int
            - Filter for equipment by their Bookable or Lendable property: 0-Both; 1-Bookable; 2-Lendable
        '''
        # Prep the params and endpoint
        params = self._create_default_params(locals())
        endpoint = self.url.get_endpoint('equipment')  
        
        # Do any necessary validation
        if not equipment_id or center_ids or modified_date_from and modified_date_to:
            raise ValueError('At least one of the following parameters must be provided: equipment_id, center_ids, modified_date_from and modified_date_to.')
        
        # Make the request
        return PaginatedAPI(self.session, endpoint, params, EquipmentResult).request()
