from api_client.models.base import Root, Body, ResponseTypes

class Headers(Body):
    response_code: str
    response_message: str


class Site(Body):
    site_id: int
    site_name: str
    address1: str
    address2: str
    city: str
    state: str
    zip_code: str
    country: str
    geographic_area: str | None
    email_address: str


class GetSitesResponse(Root):
    body: list[Site]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "sites"
        response_type = ResponseTypes.LIST