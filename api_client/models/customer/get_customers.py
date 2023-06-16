from api_client.models.base import Root, Body, ResponseTypes
from datetime import datetime, date



class Family(Body):
    family_id: int
    household_size: int
    head_of_household: str | None
    head_of_household_customer_id: int | None
    head_of_household_customer_first_name: str | None
    head_of_household_customer_last_name: str | None
    head_of_household_customer_email: str | None
    external_id: int
    family_role: str


class AlternateKey(Body):
    alternate_key_type: str
    alternate_key_status: str
    alternate_key_id: str


class Skill(Body):
    skill_id: int
    skill_title: str
    evaluation_date: str
    evaluator: str
    expiry_date: str
    evaluator_comment: str


class Customer(Body):
    customer_id: int
    encrypted_customer_id: str
    customer_title: str | None
    first_name: str
    middle_name: str
    last_name: str
    legal_name: str
    customer_type: str | None
    geographic_area: str | None
    residential_address1: str
    residential_address2: str
    residential_city: str
    residential_state_or_province: str
    residential_zip_code: str
    mailing_address1: str
    mailing_address2: str
    mailing_city: str
    mailing_state_or_province: str
    mailing_zip_code: str
    mailing_name: str
    occupation: str
    home_phone: str
    work_phone: str
    cell_phone: str
    mobile_carrier: str | None
    fax_phone: str
    pager_phone: str
    other_phone: str
    email: str
    additional_email: str
    birth_date: date | None
    age_category: str | None
    gender: str
    grade: str
    age: str
    resident_status: str | None
    residency_expire_date: date | None
    retired_status: str | None
    special_handling: bool
    head_of_household: bool
    families: list[Family]
    has_active_membership: bool
    alternate_keys: list[AlternateKey]
    emergency_contact1_first_name: str
    emergency_contact1_last_name: str
    emergency_contact1_phone: str
    emergency_contact1_relation: str
    emergency_contact1_other_phone: str
    emergency_contact2_first_name: str
    emergency_contact2_last_name: str
    emergency_contact2_phone: str
    emergency_contact2_relation: str
    emergency_contact2_other_phone: str
    no_mail: bool
    date_time_modified: datetime | None
    customer_notes: str
    customer_medical_alert: str
    customer_general_alert: str
    no_postal_mail: bool
    not_online_activated: bool
    login_created: datetime | None
    login_used: datetime | None
    interest_date: date | None
    country: str
    late_fee_date: date | None
    agree_receive_text_message: bool
    created_on: str
    photo_key: str | None
    skills: list[Skill]


class GetCustomersResponse(Root):
    body: list[Customer]

    class APIProperties:
        paginated = True
        sortable = False
        endpoint = "customers"
        response_type = ResponseTypes.LIST