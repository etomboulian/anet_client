from datetime import date, datetime
from pydantic import BaseModel
from requests_ratelimiter import LimiterSession

from api_client.models.base import Root
from api_client.utils import (
    Requester, 
    UrlBuilder, 
    HttpVerbs, 
    ApiInfo, 
    ApiException, 
    ApiResponse
)

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
    GetActivitiesResponse,
    GetActivityDetailResponse,
    GetActivityCategoriesResponse,
    GetActivityOtherCategoriesResponse,
    GetActivityFeesResponse, 
    GetActivityTypesResponse,
    GetActivityEnrollmentResponse,
    GetActivityExpandedDetailResponse,
    GetActivityDatesResponse,
    PostActivityEnrollmentPerDayResponse,
    DeleteActivityEnrollmentPerDayResponse,
    PostActivityDropInPaymentResponse,
    GetCustomersResponse,
    GetCustomQuestionsResponse,
    GetCustomQuestionAnswerResponse,
    GetProspectCustomQuestionAnswersResponse,
    GetFamilyMembersResponse
)


class SystemApiClient:
    def __init__(self, org_name: str, country: str, api_key: str, secret: str) -> None:
        self.api_info = ApiInfo(org_name, country, api_key, secret)       
        self.session = LimiterSession(per_second=2, limit_statuses=[403])
        self.url = UrlBuilder(self.api_info.org_name, self.api_info.country)  
    
    def _make_get_request(self, url_params: dict, ret_type: Root) -> Requester:
        params = self.api_info._create_default_params(url_params)
        endpoint = self.url.get_endpoint(ret_type.ApiProperties.endpoint)
        return Requester(HttpVerbs.get, self.session, endpoint, params, ret_type, None)

    def _make_post_request(self, url_params: dict, ret_type: Root, post_body: dict = None) -> Requester:
        params = self.api_info._create_default_params(url_params)
        endpoint = self.url.get_endpoint(ret_type.ApiProperties.endpoint)
        return Requester(HttpVerbs.post, self.session, endpoint, params, ret_type, post_body)
    
    def _make_delete_request(self, url_params: dict, ret_type: Root, body: dict = None) -> Requester:
        params = self.api_info._create_default_params(url_params)
        endpoint = self.url.get_endpoint(ret_type.ApiProperties.endpoint)
        return Requester(HttpVerbs.delete, self.session, endpoint, params, ret_type, body)

    def get_sites(self) -> ApiResponse:
        '''
        GetSitesAPI - Returns a list of sites for your organization (by site_name in ascending order).
        
        Notes: 
            This API does not support pagination or sorting.
        
        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        request = self._make_get_request(request_params, GetSitesResponse)
        return request()
    
    def get_organization(self) -> ApiResponse:
        '''
        GetOrganizationAPI - Returns information about the organization.
        
        Notes:
            This API does not support pagination or sorting

        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        request = self._make_get_request(request_params, GetOrganizationResponse)
        return request()
    
    def get_seasons(self) -> ApiResponse:
        '''
        GetSeasonsAPI - Returns a list of seasons for your organization (by season_name in ascending order)
        
        Notes:
            This API does not support pagination or sorting

        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        request = self._make_get_request(request_params, GetSeasonsResponse)
        return request()
    
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
        request_params = locals()
        request = self._make_get_request(request_params, GetCentersResponse)
        return request()

    def get_skills(self) -> ApiResponse:
        '''GetSkillsAPI - Returns a list of skills for your organization (by skill_id in ascending order).
        
        Notes: 
            This API does not support pagination or sorting.

        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        request = self._make_get_request(request_params, GetSkillsResponse)
        return request()

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
        request_params = locals()
        request = self._make_get_request(request_params, GetSkipDatesResponse)
        return request()
        
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

        Params: (Optional)
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
        request_params = locals()
        request = self._make_get_request(request_params, GetMembershipsResponse)
        return request()

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

        Params: (Optional)        
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
        request_params = locals()
        
        # Do any necessary validation
        if not equipment_id or center_ids or (modified_date_from and modified_date_to):
            raise ValueError('At least one of the following parameters must be provided: equipment_id, center_ids, modified_date_from and modified_date_to.')
        
        # Prep the params and endpoint
        request = self._make_get_request(request_params, GetEquipmentResponse)
        
        # Make the request
        return request()
    
    def post_validate_login(self, login_name: str, password: str) -> ApiResponse:
        '''PostValidateLoginAPI - Validates if the provided customer information can be used to log into the system. (CUI?)
        
        Notes:
            This API will retrieve one record per API call depending on the specified request parameters.
            One record will contain customer information of a customer who passes validation.

        Params: (Required)
            login_name (str): The user's login name
            password (str): The user's password in plain text

        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        post_body = {'login_name': login_name, 'password':password}
        request = self._make_post_request(request_params, PostValidateLoginResponse, post_body)
        return request()
    
    def post_forgot_password(self, email: str) -> ApiResponse:
        '''PostForgotPasswordAPI - Sends a password reset email to the acccount with the provided email address.
        
        Params:
            email (str) -> The email address of the user

        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        post_body_data = {"email": email}
        request = self._make_post_request(request_params, PostForgotResponse, post_body_data)
        return request()
    
    def post_forgot_login_name(self, email) -> ApiResponse:
        '''PostForgotLoginNameAPI - Emails the login name to the provided email address.
        
        Params: (Required)
            email (str): The email address of the user

        Returns:
            An object representing the ApiResponse

        '''
        request_params = locals()
        post_body_data = {"email": email}
        request = self._make_post_request(request_params, PostForgotResponse, post_body_data)
        return request()
    
    def get_activities(
            self,
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
            show_on_member_app: bool = None
            ) -> ApiResponse:
        '''GetActivitiesAPI - Returns a list of activities for your request parameters (by activity_id in ascending order).
        
        Notes:
            This API supports pagination, but does not support sorting.
            This API will retrieve multiple records per API call depending on the specified request parameters.
            One record will contain all information for a matching activity.

        Params: (Optional)
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
        request_params = locals()
        request = self._make_get_request(request_params, GetActivitiesResponse)
        return request()
    
    def get_activity_detail(self, activity_id: int) -> ApiResponse:
        endpoint = f"activities/{activity_id}"
        GetActivityDetailResponse.ApiProperties.endpoint = endpoint
        request = self._make_get_request(None, GetActivityDetailResponse)
        return request()

    def get_activity_categories(self, show_on_member_app: str = None) -> ApiResponse:
        request_params = locals()
        request = self._make_get_request(request_params, GetActivityCategoriesResponse)
        return request()
    
    def get_activity_other_categories(self) -> ApiResponse:
        request = self._make_get_request(None, GetActivityOtherCategoriesResponse)
        return request()
    
    def get_activity_fees(self, activity_id: int) -> ApiResponse:
        GetActivityFeesResponse.ApiProperties.endpoint = f"activities/{activity_id}/fees"
        request = self._make_get_request(None, GetActivityFeesResponse)
        return request()
    
    def get_activity_types(self, show_on_member_app: str = None) -> ApiResponse:
        request = self._make_get_request(locals(), GetActivityTypesResponse)
        return request()
    
    def get_activity_enrollment(
            self, 
            activity_id: int = None, 
            customer_ids: str = None, 
            enrollment_status: int = None, 
            date_after: datetime = None
            ) -> ApiResponse:
        request_params = locals()
        request = self._make_get_request(request_params, GetActivityEnrollmentResponse)
        return request()
    
    def get_activity_expanded_detail(
            self,
            activity_ids: int,
            enrollment_status: int = None,
            date_after: date | datetime = None
    ) -> ApiResponse:
        request_params = locals()
        request = self._make_get_request(request_params, GetActivityExpandedDetailResponse)
        return request()
    
    def get_activity_dates(
            self,
            activity_id: int
    ) -> ApiResponse:
        request_params = locals()
        request = self._make_get_request(request_params, GetActivityDatesResponse)
        return request()
    
    def post_activity_enrollment_per_day(
            self,
            activity_id: int,
            activity_date_id: int,
            customer_id: int
    ) -> ApiResponse:
        post_body = { "activity_id": activity_id, "activity_date_id": activity_date_id, "customer_id": customer_id}
        request = self._make_post_request(None, "activityenrollmentperday", PostActivityEnrollmentPerDayResponse, post_body)
        return request()
    
    def delete_activity_enrollment_per_day(
            self,
            activity_id: int,
            activity_date_id: int,
            customer_id: int,
            reservation_id: int
    ):
        post_body = { "activity_id": activity_id, "activity_date_id": activity_date_id, "customer_id": customer_id, "reservation_id": reservation_id}
        request = self._make_delete_request(None, DeleteActivityEnrollmentPerDayResponse, post_body)
        return request()

    def post_activity_drop_in_payment(
            self,
            activity_id: int,
            activity_date_id: int,
            customer_id: int,
            login_customer_id: int
            ) -> ApiResponse:
        post_body = {"activity_id": activity_id, "activity_date_id": activity_date_id, "customer_id": customer_id, "login_customer_id": login_customer_id}
        request = self._make_post_request(None, PostActivityDropInPaymentResponse, post_body)
        return request()
    
    def get_customers(
            self, 
            customer_id: int = None, 
            site_ids: str = None, 
            gender: int = None, 
            first_name: str = None, 
            last_name: str = None, 
            min_age: int = None, 
            max_age: int = None, 
            modified_date_from: date | datetime = None,
            activity_id: int = None,
            customer_ids: str = None,
            alternate_key_ids: str = None,
            prospect: bool = None
        ) -> ApiResponse:
        '''
        GetCustomersAPI - Returns a list of customers for your request parameters (by customer_id in ascending order).

        Notes:
            This API will retrieve multiple records per API call depending on the specified request parameters.
            One record will contain all information of a matching customer.

        Params:
            customer_id (int) - The ID of the customer.
            site_ids (str) - The ID of site assigned to the customer. You can specify up to 5 sites, with each site separated by a comma.
            gender (str) - Customer gender. (0-Coed, 1-Male, 2-Female, 4-Genderqueer/Androgyny, 5-Intersex, 6-Transgender, 7-Transsexual, 8-Cross-dresser, 9-FTM(female-to-male), 10-MTF(male-to-female), 11-Other).
            first_name (str) - First name of the customer. All customers whose first names start with the specified first name are returned.
            last_name (str) - Last name of the customer. All customers whose last names start with the specified last name are returned.
            min_age (int) - Customers whose age are older than or equal to the specified minimum participant age are returned.
            max_age (int) - Customers whose age are younger than or equal to the specified maximum participant age are returned.
            modified_date_from (date | datetime) - |Return a list of customers whose information was last modified on or after the specified date and time
            activity_id (int) - The ID of the activity. Customers who enrolled in the specified activity are returned.
            customer_ids (str) - You can specify up to 500 customer IDs, with each customer ID separated by a comma.
            alternate_key_ids (str) - The alternate key IDs of the customers. You can specify up to 100 alternate key IDs, with each ID separated by a comma.
            prospect (bool) - You can specify boolean value to only search prospect or non-prospect customers.

        Returns:
            An object representing the ApiResponse
        '''
        request_params = locals()
        
        if not (modified_date_from or activity_id or customer_ids or alternate_key_ids or prospect):
            raise ApiException('At least of of the parameters: modified_date_from or activity_id or customer_ids or alternate_key_ids must be provided for this API call')
        
        request = self._make_get_request(request_params, GetCustomersResponse)
        return request()

    def get_custom_questions(
            self,
            custom_question_id: int = None,
            activity_id: int = None,
            program_id: int = None,
            package_id: int = None,
            event_type_id : int = None,
            account_creation_type: int = None,
            process: int = None,
            modified_date_from: date | datetime = None,
            modified_date_to: date | datetime = None
    ) -> ApiResponse:
        '''
        GetCustomQuestionsAPI - Return a list of custom questions for your request parameters (by custom_question_id in ascending order

        '''
        request_params = locals()
        required_params = (custom_question_id, activity_id, program_id, package_id, event_type_id, process)

        required_param_count = len(list(param for param in required_params if param is not None))
        if required_param_count != 1:
            raise ApiException("Only one of custom_question_id, activity_id, program_id, package_id, event_type_id, process is required and can be specified for this API call")
        
        request = self._make_get_request(request_params, GetCustomQuestionsResponse)
        return request()
    
    def get_custom_question_answers(
            self,
            activity_id: int = None,
            package_id: int = None,
            program_id: int = None,
            permit_number: int = None,
            customer_id: int = None,
    ):
        '''
        GetCustomQuestionAnswersAPI - Return a list of custom question answers for your request parameters ((by customer_id, and then by question in ascending order).
        '''
        request_params = locals()

        required_params = (activity_id, package_id, program_id, permit_number, customer_id)
        required_param_count = len(list(param for param in required_params if param is not None))
        if required_param_count < 1:
            raise ApiException("One or more of the required parameters must be specified for this API call")
        
        request = self._make_get_request(request_params, GetCustomQuestionAnswerResponse)
        return request()
    
    def get_prospect_custom_question_answers(
            self,
            customer_ids: str
    ) -> ApiResponse:
        '''
        GetProspectCustomQuestionAnswersAPI - Return a list of prospect custom question answers for your request parameters (by customer_id in ascending order).
        '''
        request_params = locals()
        request = self._make_get_request(request_params, GetProspectCustomQuestionAnswersResponse)
        return request()
    
    def get_family_members(
            self, 
            family_ids: str
    ) -> ApiResponse:
        request_params = locals()
        request = self._make_get_request(request_params, GetFamilyMembersResponse)
        return request()