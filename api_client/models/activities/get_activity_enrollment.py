from api_client.models.base import Root, Body, ResponseTypes
from datetime import date, datetime


class Payer(Body):
    payer_first_name: str
    payer_last_name: str
    payer_customer_id: int
    payer_email: str
    payer_company_name: str
    payer_company_phone: str


class ActivityEnrollment(Body):
    activity_id: int
    activity_name: str
    enrollment_status: str
    first_name: str
    last_name: str
    customer_id: int
    customer_date_modified: datetime
    customer_email: str
    receipt_number: str
    has_active_membership: bool
    trial_class_date: date
    last_transaction_date: date
    withdraw_date: date
    total_fee: float
    total_paid: float
    total_due: int
    date_registered: datetime
    waitlisted_date: datetime
    waitlist_removed_date: date
    quantity: int
    payers: list[Payer]


class GetActivityEnrollmentResponse(Root):
    body: list[ActivityEnrollment]

    class APIProperties:
        paginated = True
        sortable = False
        endpoint = "activityenrollment"
        response_type = ResponseTypes.LIST
