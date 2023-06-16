from api_client.models.base import Root, Body, ResponseTypes


class DressingRoom(Body):
    dressing_room_id: int
    dressing_room_name: str
    dressing_room_occupant: str
    dressing_room_home_or_away_status: str


class FacilitySchedule(Body):
    facility_id: int
    facility_name: str
    facility_type: str
    facility_type_id: int
    facility_number: str
    permit_creation_date: str | None
    setup_from_time: str
    setup_to_time: str
    start_date_time: str
    end_date_time: str
    tear_down_from_time: str | None
    tear_down_to_time: str | None
    schedule_type: str
    event_type: str
    event_type_id: int
    event_description: str | None
    center_name: str
    center_id: int
    site_name: str
    site_id: int
    attendance: int
    permit_status: str
    permit_number: int
    activity_name: str
    activity_number: str
    activity_status: str
    session_name: str
    league_name: str | None
    customer_type: str
    customer_id: str | None
    customer_first_name: str | None
    customer_last_name: str | None
    has_active_membership: bool
    dressing_rooms: list[DressingRoom]
    schedule_type_id: int
    company_id: str | None
    company_name: str | None
    company_type: str | None


class GetFacilitySchedulesResponse(Root):
    body: list[FacilitySchedule]

    class APIProperties:
        paginated = True
        sortable = True
        endpoint = "facilityschedules"
        response_type = ResponseTypes.LIST