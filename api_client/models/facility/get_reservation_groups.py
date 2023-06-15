from api_client.models.base import Root, Body
from datetime import time


class Facility(Body):
    facility_id: int
    facility_name: str


class ResevationGroup(Body):
    reservation_group_id: int
    reservation_group_name: str
    event_type_name: str
    event_type_id: int
    schedule_type_name: str | None
    schedule_type_id: int | None
    non_exclusive_use: bool
    default_customer_type: str
    site_name: str | None
    site_id: int | None
    center_name: str | None
    center_id: int | None
    show_online: bool
    starting_time: time
    ending_time: time
    time_increment: int
    facilities: list[Facility]


class GetReservationGroupsResponse(Root):
    body: list[ResevationGroup]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "reservationgroups"
