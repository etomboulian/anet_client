from api_client.models.base import Root, Body
from datetime import date, datetime


class Activity(Body):
    activity_name: str
    activity_number: str
    activity_id: int
    modified_date_time: datetime
    activity_type_id: int
    activity_type: str
    parent_season_id: int
    parent_season: str
    child_season_id: int
    child_season: str
    activity_status_id: int
    activity_status: str
    activity_department_id: int
    activity_department: str
    category_id: int
    category: str
    other_category_id: int
    other_category: str
    site_id: int
    site_name: str
    default_facilities: str
    default_beginning_date: date
    default_ending_date: date
    default_pattern_dates: str
    gender_id: int
    gender: str
    enroll_min: int
    enroll_max: int
    show_on_member_app: str
    image_on_member_app: str
    age_min_year: int
    age_min_month: int
    age_min_week: int
    age_max_year: int
    age_max_month: int
    age_max_week: int


class GetActivitiesResponse(Root):
    body: list[Activity]
