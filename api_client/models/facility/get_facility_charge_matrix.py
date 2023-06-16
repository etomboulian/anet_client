from api_client.models.base import Root, Body, ResponseTypes
from datetime import date


class Headers(Body):
    response_code: str
    response_message: str


class ScheduledFeeChangeItem(Body):
    effective_date: str
    charge_amount: float


class CustomQuestion(Body):
    question_title: str
    question_text: str
    answer: str


class FacilityChargeMatrixEntry(Body):
    charge_name: str
    charge_type: str
    customer_type: str
    center_name: str
    center_id: int
    facility_name: str
    facility_id: int
    facility_type: str
    site_name: str
    site_id: int
    event_type: str
    prefill_condition: str
    gl_account: str
    discount_type: str
    system_account_package: str
    default_amount: float
    default_percentage: int
    holiday_rates: int
    unit_of_measure: str
    default_quantity: int
    once_per_permit: bool
    is_deposit: bool
    discountable: bool
    exclude_from_payment_plan: bool
    extra_booking_fee: bool
    scheduled_fee_change: list[ScheduledFeeChangeItem]
    taxable_by_tax1: bool
    taxable_by_tax2: bool
    taxable_by_tax3: bool
    taxable_by_tax4: bool
    taxable_by_tax5: bool
    taxable_by_tax6: bool
    taxable_by_tax7: bool
    taxable_by_tax8: bool
    minimum_age: int
    maximum_age: int
    alternate_key_types: str
    alternate_key_statuses: str
    online_question: str
    activation_code: str
    allow_qty_selection_online: bool
    minimum_qty_allowed: int
    maximum_qty_allowed: int
    custom_questions: list[CustomQuestion]
    activation_date: date
    expiration_date: date


class GetFacilityChargeMatrixResponse(Root):
    headers: Headers
    body: list[FacilityChargeMatrixEntry]

    class APIProperties:
        paginated = True
        sortable = True
        endpoint = "facilitychargematrix"
        response_type = ResponseTypes.LIST
