from api_client.models.base import Root, Body
from datetime import date

class RegionalPricing(Body):
    country: str
    states: str
    charge_amount: int


class GlAccount(Body):
    gl_account_name: str
    gl_account_number: str


class ScheduledFee(Body):
    effective_date: date
    charge_amount: float


class NormalCharge(Body):
    charge_name: str
    charge_type: str
    discount_order: int | None
    prefill_condition: str
    primary_fee: bool
    default_amount: float | None
    default_percentage: float | None
    customer_type: str | None
    description: str
    regional_pricings: list[RegionalPricing] | None
    gl_accounts: list[GlAccount]
    scheduled_fees: list[ScheduledFee] | None
    activation_date: date | None
    expiration_date: date | None


class GlobalDiscount(Body):
    global_discount_name: str
    global_discount_order: int | None
    global_discount_group_number: int | None
    global_discount_amount: float
    global_discount_percent: float
    global_discount_retired: bool


class GlobalSurcharge(Body):
    global_surcharge_name: str
    global_surcharge_amount: float
    global_surcharge_percent: float
    global_surcharge_retired: bool


class ActivityFees(Body):
    normal_charges: list[NormalCharge]
    global_discounts: list[GlobalDiscount]
    global_surcharges: list[GlobalSurcharge]


class GetActivityFeesResponse(Root):
    body: list[ActivityFees]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = ""
