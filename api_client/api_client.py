from datetime import date, datetime
from pydantic import BaseModel
from requests_ratelimiter import LimiterSession

from api_client.utils import Requester, UrlBuilder, HttpVerbs, ApiInfo, bool_to_str
from api_client.models import (
    GetEquipmentResponse, 
    GetOrganizationResponse, 
    GetSitesResponse, 
    GetSeasonsResponse,
    GetSkillsResponse,
    GetSkipDatesResponse,
    GetCentersResponse,
    GetMembershipsResponse,
    PostForgotResponse,
    PostValidateLoginResponse,
    GetActivitiesResponse
)
from api_client.utils.api_response import ApiResponse


class SystemApiClient:

    def __init__(self, org_name: str, country: str, api_key: str, secret: str) -> None:
        self.api_info = ApiInfo(org_name, country, api_key, secret)       
        self.session = LimiterSession(per_second=2, limit_statuses=[403])
        self.url = UrlBuilder(self.api_info.org_name, self.api_info.country)  

    def no_param_non_paginated_api_get_request(self, local_vars: dict, endpoint_name: str, ret_type: BaseModel) -> Requester:
        params = self.api_info._create_default_params(local_vars)
        endpoint = self.url.get_endpoint(endpoint_name)
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, ret_type)
        return requester

    def get_sites(self) -> ApiResponse:
        '''
        GetSitesAPI - Returns a list of sites for your organization (by site_name in ascending order).
        
        Notes: 
            This API does not support pagination or sorting.
        
        Returns:
            An object representing the ApiResponse

        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'sites', GetSitesResponse)
        return requester.request() 
    
    def get_organization(self) -> ApiResponse:
        '''
        GetOrganizationAPI - Returns information about the organization.
        
        Notes:
            This API does not support pagination or sorting

        Returns:
            An object representing the ApiResponse

        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'organization', GetOrganizationResponse)
        return requester.request() 
    
    def get_seasons(self) -> ApiResponse:
        '''
        GetSeasonsAPI - Returns a list of seasons for your organization (by season_name in ascending order)
        
        Notes:
            This API does not support pagination or sorting

        Returns:
            An object representing the ApiResponse

        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'seasons', GetSeasonsResponse)
        return requester.request()
    
    def get_centers(self, show_on_member_app: bool = None) -> ApiResponse:
        '''
        GetCentersAPI
            - Returns a list of centers for your organization (by center_name in ascending order).
            - This API does not support pagination or sorting

        Params:
            show_on_member_app (bool): Filter for centers by their 'Show On the ACTIVE Net Captivate App' flag: Y or N.
        
        Returns:
            An object representing the ApiResponse

        '''
        params = self.api_info._create_default_params(locals())
        endpoint = self.url.get_endpoint('centers')  
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetCentersResponse)
        return requester.request()

    def get_skills(self) -> ApiResponse:
        '''GetSkillsAPI - Returns a list of skills for your organization (by skill_id in ascending order).
        
        Notes: 
            This API does not support pagination or sorting.

        Returns:
            An object representing the ApiResponse

        '''
        requester = self.no_param_non_paginated_api_get_request(locals(), 'skills', GetSkillsResponse)
        return requester.request()

    def get_skip_dates(self, facility_id: int) -> ApiResponse:
        '''GetSkipDatesAPI - Returns a list of skip dates for the specified facility (by start date in ascending order).
        
        Notes:
            This API supports pagination and sorting.
            You can sort the results by one of the following parameters
                start_date -> The start date of skip dates. Order option: ascending or descending.
                start_time -> The start time of skip dates. Order option: ascending or descending.

        Params:
            facility_id (int): The facility id of the facility.

        Returns:
            An object representing the ApiResponse

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
            ) -> ApiResponse:
        '''GetMembershipsAPI - Returns membership information for your request parameters (by membership_id in ascending order).
        
        Notes:
            This API supports pagination, but does not support sorting.
            The modified_date_from and modified_date_to are required request parameters if you do not specify Package ID or Customer ID. 
            The modified_date_to must be a date and time on or after modified_date_from, and the modified_date_to must be within 3 days after the modified_date_from.

        Params:
            customer_id (int): Customer ID
            package_id (int): Package ID
            modified_date_from (datetime | date): Memberships last updated on or after the specified date and time are returned (HH:MM is optional)
            modified_date_to (datetime | date): Memberships last updated on or before the specified date and time are returned (HH:MM is optional).
            package_status_id (int): Memberships with packages in the specified status (0-Open, 1-Closed) are returned.
            active_memberships_only (bool): Specify 'Y' to search for only active memberships.
            encode_customer_id (str): Encoded Customer ID (only used if customer_id parameter not passed)            

        Returns:
            An object representing the ApiResponse

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
        modified_date_from: date | datetime = None,
        modified_date_to: date | datetime = None,
        show_on_member_app: bool = None,
        open_block_date_from: date = None,
        ) -> ApiResponse:
        '''GetEquipmentAPI - Returns a list of equipment items for the specified request parameters (by equipment_id in ascending order by default).
        
        Notes:
            This API supports pagination, but does not support sorting. 
            At least one of the following parameters must be provided to this method: 'equipment_id', 'center_ids', 'modified_date_from' and 'modified_date_to'.

        Params:        
            equipment_id (int): The ID of the equipment item
            center_ids (string): You can specify up to 5 center IDs, with each center ID separated by a comma.
            bookable_or_lendable (int): Filter for equipment by their Bookable or Lendable property: 0-Both 1-Bookable 2-Lendable
            modified_date_from (date|datetime): Equipment whose latest update is on or after the specified date and time are returned 
            modified_date_to (date): Equipment whose latest update is on or before the specified date and time are returned 
            show_on_member_app (bool): To retrieve equipment items which are displayed in the ACTIVE Net Captivate app, specify 'Y' or 'N'
            open_block_date_from (date): The begin date for get open block dates.
        
        Returns:
            An object representing the ApiResponse
        
        '''
        # Prep the params and endpoint
        params = self.api_info._create_default_params(locals())
    
        if bookable_lendable := params.get('bookable_or_lendable', None) is not None: 
            params['bookable_or_lendable'] = bool_to_str(bookable_or_lendable)
    
        endpoint = self.url.get_endpoint('equipment')  
        
        # Do any necessary validation
        if not equipment_id or center_ids or modified_date_from and modified_date_to:
            raise ValueError('At least one of the following parameters must be provided: equipment_id, center_ids, modified_date_from and modified_date_to.')
        
        # Make the request
        requester = Requester(HttpVerbs.get, self.session, endpoint, params, GetEquipmentResponse)
        return requester.request()
    
    def post_validate_login(self, login_name: str, password: str) -> ApiResponse:
        '''PostValidateLoginAPI - Validates if the provided customer information can be used to log into the system. (CUI?)
        
        Notes:
            This API will retrieve one record per API call depending on the specified request parameters.
            One record will contain customer information of a customer who passes validation.

        Params:
            login_name (str) -> The user's login name
            password (str) -> The user's password in plain text

        Returns:
            An object representing the ApiResponse

        '''
        params = self.api_info._create_default_params(None)
        endpoint = self.url.get_endpoint('validatelogin') 
        
        post_body = {'login_name': login_name, 'password':password}

        requester = Requester(HttpVerbs.post, self.session, endpoint, params, PostValidateLoginResponse, post_body=post_body)
        return requester.request()
    
    def post_forgot_password(self, email: str) -> ApiResponse:
        '''PostForgotPasswordAPI - Sends a password reset email to the acccount with the provided email address.
        
        Params:
            email (str) -> The email address of the user

        Returns:
            An object representing the ApiResponse

        '''
        params = self.api_info._create_default_params(None)
        endpoint = self.url.get_endpoint('forgotpassword')
        post_body = {"email": email}
        requester = Requester(HttpVerbs.post, self.session, endpoint, params, PostForgotResponse, post_body)
        return requester.request()
    
    def post_forgot_login_name(self, email) -> ApiResponse:
        '''PostForgotLoginNameAPI - Emails the login name to the provided email address.
        
        Params:
            email (str): The email address of the user

        Returns:
            An object representing the ApiResponse

        '''
        params = self.api_info._create_default_params(None)
        endpoint = self.url.get_endpoint('forgotloginname')
        post_body = {"email": email}
        requester = Requester(HttpVerbs.post, self.session, endpoint, params, PostForgotResponse, post_body)
        return requester.request()
    
    
    def get_activities(self,
                       activity_name: str = None,
                       activity_number: str = None,
                       activity_type_id: int = None,
                       parent_season_id: int = None,
                       activity_status_id: int = None,
                       category_id: int = None,
                       other_category_id: int = None,
                       site_ids: str = None,
                       center_ids: str = None,
                       days_of_week: str = None,
                       first_date_range_from: date = None,
                       first_date_range_to: date = None,
                       last_date_range_from: date = None,
                       last_date_range_to: date = None,
                       modified_date_from: date | datetime = None,
                       modified_date_to: date | datetime = None,
                       gender: int = None,
                       age_from: int = None,
                       age_to: int = None,
                       skill_id: int = None,
                       show_on_member_app: bool = None) -> ApiResponse:
        '''GetActivitiesAPI - Returns a list of activities for your request parameters (by activity_id in ascending order).
        
        Notes:
            This API supports pagination, but does not support sorting.
            This API will retrieve multiple records per API call depending on the specified request parameters.
            One record will contain all information for a matching activity.

        Params (Optional):
            activity_name (str): Activity name. All activities whose names fully or partially match the specified name are returned.
            activity_number (int): Activity number. All activities whose activity numbers fully or partially match the specified activity number are returned.
            activity_type_id (int): The ID of the activity type.
            parent_season_id (int): The ID of the activity parent season.
            activity_status_id (int): You can only specify one activity status: 0-Open, 1-Closed, 2-Cancelled, 3-Tentative, 4-On Hold, 5-Retired, 6-Date Conflicted
            category_id (int): The ID of the activity category.
            other_category_id (int): The ID of the activity other category.
            site_ids (str): The IDs of the sites assigned to the activity. You can specify up to 5 sites, with each site separated by a comma.
            center_ids (str): The center ID for the activity’s facilities. You can specify up to 5 centers, with each center separated by a comma.
            days_of_week (str): If a meeting date is within the specified days of the week, then the activity is returned. (e.g. If the days of the week are Mon and Wed, the specified string should be 0101000)
            first_date_range_from (date): Activities whose first meeting date is on or after the specified date are returned.
            first_date_range_to (date): Activities whose first meeting date is on or before the specified date are returned.
            last_date_range_from (date): Activities whose last meeting date is on or after the specified date are returned.
            last_date_range_to (date): Activities whose last meeting date is on or before the specified date are returned.
            modified_date_from (date|datetime): Activities last updated on or after the specified date and time are returned (HH:MM is optional).
            modified_date_to (date|datetime): Activities last updated on or before the specified date and time are returned (HH:MM is optional).
            gender (int): Genders eligible for registration. (0-Coed, 1-Male, 2-Female, 4-Genderqueer/Androgyny, 5-Intersex, 6-Transgender, 7-Transsexual, 8-Cross-dresser, 9-FTM(female-to-male), 10-MTF(male-to-female), 11-Other).
            age_from (int): Activities whose age ranges are fully or partially within the specified age range are returned.
            age_to (int): Activities whose age ranges are fully or partially within the specified age range are returned.
            skill_id (int): The ID of the skill. Activities whose configured skills include the skill specified are returned. Call GetSkills API to get the skill_id.
            show_on_member_app (str): Filter for activities by their 'Show On The ACTIVE Net Captivate App' flag: Y or N

        Returns:
            An object representing the ApiResponse

        '''
        pass