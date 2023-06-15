from api_client.models.base import Root, Body
from datetime import datetime, date

class OpenBlock(Body):
    date: date
    time_block_on_date: str


class CalculatedOpenPatternItem(Body):
    date_range: str
    days_of_week: str
    opening_times: str


class Facility(Body):
    facility_id: int
    modified_date_time: datetime
    facility_number: str
    facility_name: str
    prevent_further_use: bool
    description: str
    facility_type: str
    center_name: str
    center_id: int
    default_minimum_capacity: int
    default_maximum_capacity: int
    reserve_by: str
    start_on: datetime | None
    disclaimer: str
    prep_code: str | None
    setup_time: int
    teardown_time: int
    hide_on_internet: bool
    amenities: str
    capacity_track_current_in: int
    capacity_track_maximum: int
    show_on_member_app: str
    member_app_image: str
    open_blocks: list[OpenBlock]
    calculated_open_pattern: list[CalculatedOpenPatternItem] | None


class GetFacilitiesResponse(Root):
    body: list[Facility]

    class ApiProperties:
        paginated = True
        sortable = True
        endpoint = "facilities"
