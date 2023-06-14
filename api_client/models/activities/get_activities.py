from api_client.models.base import Root, Body
from datetime import date, datetime


class Activity(Body):
    activity_name: str
    activity_number: str
    activity_id: int
    modified_date_time: datetime
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
    site_id: int
    site_name: str
    default_facilities: str | None
    default_beginning_date: date
    default_ending_date: date
    default_pattern_dates: str
    gender_id: int
    gender: str
    enroll_min: int | None
    enroll_max: int | None
    show_on_member_app: str
    image_on_member_app: str
    age_min_year: int | None
    age_min_month: int | None
    age_min_week: int | None
    age_max_year: int | None
    age_max_month: int | None
    age_max_week: int | None


class GetActivitiesResponse(Root):
    body: list[Activity]

    class ApiProperties:
        paginated = True
        sortable = False
        endpoint = "activities"
