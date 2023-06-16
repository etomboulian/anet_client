from api_client.models.base import Root, Body, ResponseTypes
from datetime import date

class Headers(Body):
    response_code: str
    response_message: str


class PatternDate(Body):
    pattern_date: str


class ActivityPattern(Body):
    pattern_name: str
    beginning_date: str
    ending_date: str
    weeks_of_month: str
    pattern_dates: list[PatternDate]


class Family(Body):
    family_id: int
    head_of_household: str | None
    head_of_household_customer_id: int | None
    head_of_household_customer_first_name: str | None
    head_of_household_customer_last_name: str | None
    head_of_household_customer_email: str | None


class Payer(Body):
    payer_first_name: str
    payer_last_name: str
    payer_customer_id: int
    payer_email: str
    payer_company_name: str | None
    payer_company_phone: str | None


class QuestionAnswer(Body):
    question_title: str
    question_text: str
    question_id: int
    answer: str
    time_stamp: str


class ActivityExpandedDetail(Body):
    activity_id: int
    activity_name: str
    activity_status: str
    activity_category: str | None
    activity_other_category: str | None
    activity_patterns: list[ActivityPattern]
    first_name: str
    last_name: str
    customer_id: int
    customer_email: str
    trial_class_date: date | None
    enrollment_status: str
    date_registered: str
    has_active_membership: bool
    home_phone: str
    work_phone: str
    cell_phone: str
    mobile_carrier: str | None
    age: str
    age_category: str | None
    gender: str
    residential_address1: str
    residential_address2: str
    residential_city: str
    residential_state_or_province: str
    residential_zip_code: str
    families: list[Family]
    payers: list[Payer]
    question_answers: list[QuestionAnswer] | None


class GetActivityExpandedDetailResponse(Root):
    body: list[ActivityExpandedDetail]

    class APIProperties:
        paginated = True
        sortable = False
        endpoint = "activityexpandeddetail"
        response_type = ResponseTypes.LIST