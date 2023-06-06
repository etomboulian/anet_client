from datetime import date, datetime
from typing import Any
from api_client.models.base import Root, Body


class Membership(Body):
    customer_id: int
    package_id: int
    customer_first_name: str | None
    customer_last_name: str | None
    customer_since_date: date | None
    primary_member_first_name: str | None
    primary_member_last_name: str | None
    member_since_date: date | None
    membership_id: int
    primary_member_customer_id: int
    membership_status: str | None
    effective_date: date | None
    expiration_date: date | None
    automatic_renewal: bool
    last_renewed_date: date | None
    suspended_from_date: date | None
    suspended_until_date: date | None
    scheduled_automatic_cancellation: str
    scheduled_automatic_cancellation_date: date | None
    automatic_cancellation_reason: str
    scheduled_cancellation: str
    scheduled_cancellation_date: date | None
    scheduled_cancellation_reason: str
    total_number_of_uses: int | None
    number_of_uses_used: int | None
    remaining_number_of_uses_left: int | None
    package_name: str
    package_status_id: int
    package_site_id: int | None
    package_category_id: int
    family_package: bool
    entry_point: Any
    package_retention_eligible: bool
    member_pass_number: str
    primary_member_pass_number: str
    suspension_reason: str
    cancellation_date: date | None
    cancellation_reason: str
    modified_date_time: datetime | None
    qualify_member_registration_dates: bool


class GetMembershipsResponse(Root):
    body: list[Membership]

    class ApiProperties:
        paginated = True
        sortable = False