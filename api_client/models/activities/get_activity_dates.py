from api_client.models.base import Root, Body
from datetime import datetime


class ActivityDate(Body):
    activity_id: int
    activity_date_id: int
    activity_facility_id: int
    activity_facility_name: str
    activity_center_id: int
    activity_center_name: str
    start_date_time: datetime
    end_date_time: datetime
    available_spots: int


class GetActivityDatesResponse(Root):
    body: list[ActivityDate]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "activitydates"
