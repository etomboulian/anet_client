from api_client.models.base import Root, Body, ResponseTypes


class FacilityType(Body):
    description: str
    prevent_further_use: bool
    hide_on_internet: bool
    facility_type_id: int


class GetFacilityTypesResponse(Root):
    body: list[FacilityType]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "facilitytypes"
        response_type = ResponseTypes.LIST
        