from api_client.models.base import Root, Body
from datetime import date

class GlAccount(Body):
    gl_account_name: str
    gl_account_number: str


class ScheduledFee(Body):
    effective_date: str
    charge_amount: int


class PackageFee(Body):
    charge_name: str
    charge_type: str
    discount_order: int
    prifill_condition: str
    primary_fee: bool
    default_amount: float
    default_percentage: float
    customer_type: str
    description: str
    gl_accounts: list[GlAccount]
    scheduled_fees: list[ScheduledFee]
    activation_date: date
    expiration_date: date


class GlobalDiscount(Body):
    global_discount_name: str
    global_discount_order: int
    global_discount_group_number: int
    global_discount_amount: int
    global_discount_percent: int
    global_discount_retired: bool


class MembershipPackageFees(Body):
    package_fees: list[PackageFee]
    global_discounts: list[GlobalDiscount]


class GetMembershipPackageFeesResponse(Root):
    body: list[MembershipPackageFees]

    class ApiProperties:
        paginated = False
        sortable = False