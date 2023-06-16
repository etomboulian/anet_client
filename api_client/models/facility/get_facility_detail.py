from api_client.models.base import Root, Body, ResponseTypes


class EventCapacity(Body):
    event_type_id: int
    event_type_description: str
    minimum_capacity: int
    maximum_capacity: int


class FacilityExtraDetail(Body):
    extra_detail_description: str
    detail_name: str
    data_url: str


class FacilityRentalBlock(Body):
    block_description: str
    block_start_time: str
    block_end_time: str


class FacilityDateRange(Body):
    date_range_description: str
    date_range_start_date: str
    date_range_end_date: str


class SubFacility(Body):
    facility_id: int
    facility_name: str


class EntryPoint(Body):
    entry_point_id: int
    entry_point_name: str


class DressingRoom(Body):
    dressing_room_id: int
    dressing_room_name: str


class FacilityDetail(Body):
    facility_id: int
    facility_number: str
    facility_name: str
    prevent_further_use: bool
    description: str
    facility_type: str
    center_name: str
    center_id: int
    address1: str
    address2: str
    city: str
    state: str
    zip_code: str
    latitude: str
    longitude: str
    default_minimum_capacity: int
    default_maximum_capacity: int
    event_capacities: list[EventCapacity]
    maximum_attendance_at_one_time: int
    reserve_by: str
    start_on: str | None
    minimum_reservation_time: str
    maximum_reservation_time: str
    internet_reservation_type: int
    internet_reservation_process: int
    disclaimer: str
    disclaimer_text: str
    prep_code: str | None
    setup_time: int
    teardown_time: int
    hide_on_internet: bool
    prohibit_internet_permits: bool
    exclude_from_league_scheduling: bool
    max_per_cust_per_day_per_facility: int
    musco_lighting_id: str
    sklogix_lighting_id: str
    facility_notes: str
    aui_reservation_min_limit: str
    aui_reservation_max_limit: str
    cui_reservation_min_limit: str
    cui_reservation_min_limit_nonresident: str
    cui_reservation_max_limit: str
    cui_reservation_max_limit_nonresident: str
    online_reservation_open_time: str | None
    amenities: str
    checkin_time: str | None
    checkout_time: str | None
    facility_extra_details: list[FacilityExtraDetail]
    facility_rental_blocks: list[FacilityRentalBlock]
    facility_date_ranges: list[FacilityDateRange]
    facility_users: str | None
    facility_final_approvers: str | None
    display_on_map: bool
    sub_facilities: list[SubFacility]
    entry_points: list[EntryPoint]
    dressing_rooms: list[DressingRoom] | None


class GetFacilityDetailResponse(Root):
    body: list[FacilityDetail]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "facilities/{facility_id}"
        response_type = ResponseTypes.SINGLE