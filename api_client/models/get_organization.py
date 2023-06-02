
from pydantic import BaseModel

from api_client.models.base import Body, Root


class Organization(Body):
    organization_id: int | None
    name: str | None
    time_zone: str | None
    logo_on_member_app: str | None
    country: str
    retired: str | None
    cui_url: str | None


class GetOrganizationResponse(Root):
    body: list[Organization]

    class ApiProperties:
        paginated = False
        sortable = False