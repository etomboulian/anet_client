from datetime import date
from pydantic import BaseModel
from requests_ratelimiter import LimiterSession

from client.utils import Requester, UrlBuilder, HttpVerbs, ApiInfo
from client.models import GetEquipmentResult, GetOrganizationResult, GetSitesResult


class SystemApiClient:

    def __init__(self, org_name: str, country: str, api_key: str, secret: str) -> None:
        self.api_info = ApiInfo(org_name, country, api_key, secret)       
        self.session = LimiterSession(per_second=2, limit_statuses=[403])
        self.url = UrlBuilder(self.api_info.org_name, self.api_info.country)  

    def no_param_non_paginated_api_get_request(self, local_vars: dict, endpoint_name: str, ret_type: BaseModel):
        params = self.api_info._create_default_params(local_vars)
        endpoint = self.url.get_endpoint(endpoint_name)
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, ret_type)
        return requester

    def get_sites(self):
        requester = self.no_param_non_paginated_api_get_request(locals(), 'sites', GetSitesResult)
        return requester.request() 
        # params = self.api_info._create_default_params(locals())
        # endpoint = self.url.get_endpoint('sites')  
        # requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetSitesResult)
        # return requester.request()
    
    def get_organization(self):
        requester = self.no_param_non_paginated_api_get_request(locals(), 'organization', GetOrganizationResult)
        return requester.request() 
    
    def get_centers(self):
        pass

    def get_skills(self):
        pass

    def get_skip_dates(self):
        pass

    def get_memberships(self):
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
        ** Note: At least one of the following parameters must be provided to this method: 
        'equipment_id', 'center_ids', 'modified_date_from' and 'modified_date_to'.

        Retrieves an object representing the request to the Active Net Get Equipment API Endpoint

        param: equipment_id | int | The ID of the equipment item
        param: center_ids | string | You can specify up to 5 center IDs, with each center ID separated by a comma.
        param: bookable_or_lendable  | int | Filter for equipment by their Bookable or Lendable property: 0-Both 1-Bookable 2-Lendable
        param: modified_date_from  | date |
        param: modified_date_to  | date |
        param: show_on_member_app  | bool |
        param: open_block_date_from  | date |
        '''
        # Prep the params and endpoint
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('equipment')  
        
        # Do any necessary validation
        if not equipment_id or center_ids or modified_date_from and modified_date_to:
            raise ValueError('At least one of the following parameters must be provided: equipment_id, center_ids, modified_date_from and modified_date_to.')
        
        # Make the request
        return Requester(HttpVerbs.get, self.session, endpoint, params, GetEquipmentResult).request()
