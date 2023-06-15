from api_client.models.base import Root, Body
from datetime import time

class DayTimeItem(Body):
    weekday: str
    opens: time
    closes: time
    closed_all_day: bool


class DefaultSetting(Body):
    open_24_hours: bool
    default_opens: time
    default_closes: time
    day_time: list[DayTimeItem]


class DayTimeItem(Body):
    weekday: str
    opens: time | None
    closes: time | None
    closed_all_day: bool


class OverrideSetting(Body):
    description: str
    date_range: str
    open_24_hours: bool
    day_time: list[DayTimeItem]


class FacilityOpenHours(Body):
    default_settings: list[DefaultSetting]
    override_settings: list[OverrideSetting]


class GetFacilityOpenHoursResponse(Root):
    body: list[FacilityOpenHours]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "facilityopenhours/{facility_id}"
