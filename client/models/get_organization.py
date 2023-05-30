
from pydantic import BaseModel

from client.models.base import Body, Root


class Organization(Body):
    organization_id: int | None
    name: str | None
    time_zone: str | None
    logo_on_member_app: str | None
    country: str
    retired: str | None
    cui_url: str | None


class GetOrganizationResult(Root):
    body: list[Organization]
