from datetime import date, datetime
from pydantic import BaseModel
from requests_ratelimiter import LimiterSession

from api_client.utils import Requester, UrlBuilder, HttpVerbs, ApiInfo
from api_client.models import (
    GetEquipmentResponse, 
    GetOrganizationResponse, 
    GetSitesResponse, 
    GetSeasonsResponse,
    GetSkillsResponse,
    GetSkipDatesResponse,
    GetCentersResponse,
    GetMembershipsResponse
)


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
        '''
        GetSitesAPI  
            - Returns a list of sites for your organization (by site_name in ascending order).
            - This API does not support pagination or sorting.

        Parameters:
            - None
        
        Returns:
            - ApiResponse object
        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'sites', GetSitesResponse)
        return requester.request() 
    
    def get_organization(self):
        '''
        GetOrganizationAPI
            - Returns information about the organization.
            - This API does not support pagination or sorting

        Parameters:
            - None

        Returns:
            - ApiResponse object    
        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'organization', GetOrganizationResponse)
        return requester.request() 
    
    def get_seasons(self):
        '''
        GetSeasonsAPI
            - Returns a list of seasons for your organization (by season_name in ascending order)
            - This API does not support pagination or sorting

        Parameters:
            - None

        Returns:
            - ApiResponse object
        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'seasons', GetSeasonsResponse)
        return requester.request()
    
    def get_centers(self, show_on_member_app: bool = None):
        '''
        GetCentersAPI
            - Returns a list of centers for your organization (by center_name in ascending order).
            - This API does not support pagination or sorting

        Parameters:
            - show_on_member_app (bool) [optional] -> Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag: Y or N.
        
        Returns:
            - ApiResponse object
        '''
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('centers')  
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetCentersResponse)
        return requester.request()

    def get_skills(self):
        '''
        GetSkillsAPI
            - Returns a list of skills for your organization (by skill_id in ascending order).
            - This API does not support pagination or sorting.

        Parameters:
            - None

        Returns:
            - ApiResponse object
        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'skills', GetSkillsResponse)
        return requester.request()

    def get_skip_dates(self, facility_id: int):
        '''
        GetSkipDatesAPI
            - Returns a list of skip dates for the specified facility (by start date in ascending order).
            - This API supports pagination and sorting.
                You can sort the results by one of the following parameters
                - start_date -> The start date of skip dates. Order option: ascending or descending.
                - start_time -> The start time of skip dates. Order option: ascending or descending.

        Parameters:
            - facility_id (int) [mandatory] -> The facility id of the facility.

        Returns:
            - ApiResponse object
        '''
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('skipdates')  
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetSkipDatesResponse)
        return requester.request()
        

    def get_memberships(
            self,
            customer_id: int = None,
            package_id: int = None,
            modified_date_from: datetime | date = None,
            modified_date_to: datetime | date = None,
            package_status_id: int = None,
            active_memberships_only: bool = None,
            encode_customer_id: str = None
            ):
        '''
        GetMembershipsAPI
            - Returns membership information for your request parameters (by membership_id in ascending order).
            - This API supports pagination, but does not support sorting.

        Parameters:
            - customer_id (int) [optional] -> Customer ID
            - package_id (int) [optional] -> Package ID
            - modified_date_from (datetime | date) [optional] -> Memberships last updated on or after the specified date and time are returned (HH:MM is optional)
            - modified_date_to (datetime | date) [optional] -> Memberships last updated on or before the specified date and time are returned (HH:MM is optional).
            - package_status_id (int) [optional] = None,
            - active_memberships_only (bool) [optional] = None,
            - encode_customer_id (str) [optional] = None

         Validation Rules:
            - The modified_date_from and modified_date_to are required request parameters if you do not specify Package ID or Customer ID. 
            - The modified_date_to must be a date and time on or after modified_date_from, and the modified_date_to must be within 3 days after the modified_date_from.

        Returns:
            - ApiResponse object
        '''
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('memberships')
        

        requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetMembershipsResponse)
        return requester.request()

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
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetEquipmentResponse)
        return requester.request()
