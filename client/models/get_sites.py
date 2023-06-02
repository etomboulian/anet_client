from pydantic import BaseModel

from client.models.base import Root

class Headers(BaseModel):
    response_code: str
    response_message: str


class Site(BaseModel):
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

    class ApiProperties:
        paginated = False
        sortable = False