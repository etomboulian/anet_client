from api_client.models.base import Root, Body
from datetime import date, datetime, time


class QualifiedFacility(Body):
    facility_id: int
    facility_name: str


class QualifiedFacilityType(Body):
    facility_type_id: int
    description: str


class EventTypes(Body):
    event_type_id: int
    event_type_description: str
    prep_code: str | None
    setup_time: int | None
    teardown_time: int | None
    schedule_type_id: int
    schedule_type_description: str
    site_id: int | None
    site_name: str | None
    prevent_further_use: bool
    hide_on_internet: bool
    allow_non_exclusive_use: bool
    available_for_all_facilities: bool
    qualified_facilities: list[QualifiedFacility]
    qualified_facility_types: list[QualifiedFacilityType]


class GetEventTypesResponse(Root):
    body: list[EventTypes]
    
    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "eventtypes"
