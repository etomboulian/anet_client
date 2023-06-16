from api_client.models.base import Root, Body, ResponseTypes

class MembershipPackageCategory(Body):
    category_id: int
    category_name: str
    description: str
    retention_eligible: bool
    qualify_commission: bool


class GetMembershipPackageCategoryResponse(Root):
    body: list[MembershipPackageCategory]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = 'membershippackagecategories'
        response_type = ResponseTypes.LIST
