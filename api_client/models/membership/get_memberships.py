from api_client.models.base import Root, Body, ResponseTypes
from datetime import date

class Membership(Body):
    customer_id: int
    package_id: int
    customer_first_name: str
    customer_last_name: str
    customer_since_date: date | None
    primary_member_first_name: str
    primary_member_last_name: str
    member_since_date: date
    membership_id: int
    primary_member_customer_id: int
    membership_status: str
    effective_date: date
    expiration_date: date
    automatic_renewal: bool
    last_renewed_date: date | None
    suspended_from_date: date | None
    suspended_until_date: date | None
    scheduled_automatic_cancellation: str
    scheduled_automatic_cancellation_date: date
    automatic_cancellation_reason: str
    scheduled_cancellation: str
    scheduled_cancellation_date: date
    scheduled_cancellation_reason: str
    total_number_of_uses: int
    number_of_uses_used: int
    remaining_number_of_uses_left: int
    package_name: str
    package_status_id: int
    package_site_id: int
    package_category_id: int
    family_package: bool
    entry_point: str
    package_retention_eligible: bool
    member_pass_number: str
    primary_member_pass_number: str
    suspension_reason: str
    cancellation_date: date
    cancellation_reason: str
    modified_date_time: str
    qualify_member_registration_dates: bool


class GetMembershipsResponse(Root):
    body: list[Membership]

    class APIProperties:
        paginated = True
        sortable = False
        endpoint = "memberships"
        response_type = ResponseTypes.LIST
