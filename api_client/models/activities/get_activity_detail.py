from api_client.models.base import Root, Body
from datetime import date, datetime


class PatternFacility(Body):
    facility_name: str
    facility_id: int
    center_name: str
    center_id: int


class PatternDate(Body):
    pattern_date: str


class PreparationCode(Body):
    preparation_code_name: str | None
    setup_time: int
    cleanup_time: int


class ActivityPattern(Body):
    pattern_name: str
    pattern_facilities: list[PatternFacility]
    event_notes: str
    beginning_date: str
    ending_date: str
    weeks_of_month: str
    pattern_dates: list[PatternDate]
    preparation_code: PreparationCode


class PriorityEnrollmentDatetimes(Body):
    first_daytime_person: datetime | None
    first_daytime_person_nonresidents: datetime | None
    first_daytime_members: datetime | None
    last_daytime_person: datetime | None
    first_daytime_internet: datetime | None
    first_daytime_internet_nonresidents: datetime | None
    first_daytime_internet_members: datetime | None
    last_daytime_internet: datetime | None


class EnrollmentDatetime(Body):
    first_daytime_person: datetime | None
    first_daytime_person_nonresidents: datetime | None
    first_daytime_members: datetime | None
    last_daytime_person: datetime | None
    first_daytime_internet: datetime | None
    first_daytime_internet_nonresidents: datetime | None
    first_daytime_internet_members: datetime | None
    last_daytime_internet: datetime | None


class Skill(Body):
    skill_id: int
    skill_title: str
    skill_description: str
    available_for: str


class Organization(Body):
    guid: str
    name: str
    url: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    fax: str
    email: str
    phone: str


class ActivityExclusion(Body):
    exclusion_start_date: str
    exclusion_end_date: str


class ActivityRecurrence(Body):
    activity_start_date: str
    activity_start_time: str
    activity_end_date: str
    activity_end_time: str
    frequency: str
    days: str
    activityExclusions: list[ActivityExclusion]


class Place(Body):
    name: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    country: str


class PrerequisitesMembershipItem(Body):
    prerequisite_id: int
    group_number: int
    package_id: int
    package_name: str


class ActivityDetail(Body):
    activity_name: str
    activity_number: str
    external_event_number: str
    activity_id: int
    asset_id: str
    public_url: str
    activity_type_id: int
    activity_type: str
    parent_season_id: int | None
    parent_season: str | None
    child_season_id: int | None
    child_season: str | None
    activity_status_id: int
    activity_status: str
    activity_department_id: int | None
    activity_department: str | None
    category_id: int | None
    category: str | None
    other_category_id: int | None
    other_category: str | None
    catalog_description: str
    tax_receipt_eligibility: bool
    usage_fee_name: str
    site_name: str
    site_id: int
    location_description: str
    default_beginning_date: str
    default_ending_date: str
    date_description: str | None
    activity_patterns: list[ActivityPattern]
    number_of_meeting_dates: int
    number_of_weeks: int
    number_of_enrolled: int
    open_spaces: str
    open_spaces_online: str
    gender_id: int
    gender: str
    age_min_year: int | None
    age_min_month: int | None
    age_min_week: int | None
    age_max_year: int | None
    age_max_month: int | None
    age_max_week: int | None
    min_grade: str | None
    max_grade: str | None
    age_calc_date: str | None
    alternate_key_type: str
    alternate_key_status: str
    enroll_max: int | None
    enroll_min: int | None
    priority_enrollment_datetimes: PriorityEnrollmentDatetimes
    enrollment_datetimes: list[EnrollmentDatetime]
    user_notes: str
    online_notes: str
    receipt_notes: str
    no_internet_reg: bool
    hide_on_internet: bool
    no_qty_based_enrollment: bool
    use_pass_or_fail: bool
    show_price_info_online: bool
    show_scholarship_online: bool
    allow_waiting_list: bool
    online_new_activity: bool
    online_new_until: str | None
    instructors: str | None
    supervisor: str | None
    skills: list[Skill]
    allow_private_lesson_bookings: bool
    parent_activity_name: str | None
    parent_activity_number: str | None
    top_parent_activity_name: str
    top_parent_activity_number: str
    sub_activity_number: str
    organization: Organization
    activity_recurrences: list[ActivityRecurrence]
    place: Place
    show_on_member_app: str
    member_app_image: str
    prerequisites_membership: list[PrerequisitesMembershipItem]
    dropin_fee_charge_amount: int | None
    allow_dropin: str


class GetActivityDetailResponse(Root):
    body: list[ActivityDetail]

    class ApiProperties:
        paginated = False
        sortable = False
