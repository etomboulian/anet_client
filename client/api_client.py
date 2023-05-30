from datetime import date
from requests_ratelimiter import LimiterSession
from client.api_info import ApiInfo
from client.models.get_equipment import GetEquipmentResult
from client.models.get_organization import GetOrganizationResult
from client.models.get_sites import GetSitesResult
from client.utils import PaginatedAPI
from client.utils import UrlBuilder


class SystemApiClient:

    def __init__(self, org_name: str, country: str, api_key: str, secret: str) -> None:
        self.api_info = ApiInfo(org_name, country, api_key, secret)       
        self.session = LimiterSession(per_second=2)
        self.url = UrlBuilder(self.api_info.org_name, self.api_info.country)  

    def get_sites(self):
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('sites')  
        return PaginatedAPI(self.session, endpoint, params, GetSitesResult).request()
    
    def get_organization(self):
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('organization')
        return PaginatedAPI(self.session, endpoint, params, GetOrganizationResult).request()
    
    def get_centers(self):
        pass

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
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('equipment')  
        
        # Do any necessary validation
        if not equipment_id or center_ids or modified_date_from and modified_date_to:
            raise ValueError('At least one of the following parameters must be provided: equipment_id, center_ids, modified_date_from and modified_date_to.')
        
        # Make the request
        return PaginatedAPI(self.session, endpoint, params, GetEquipmentResult).request()
