from api_client.models.base import Body, Root, ResponseTypes


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

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "organization"
        response_type = ResponseTypes.SINGLE