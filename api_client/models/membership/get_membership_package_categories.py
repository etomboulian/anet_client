from api_client.models.base import Root, Body

class MembershipPackageCategory(Body):
    category_id: int
    category_name: str
    description: str
    retention_eligible: bool
    qualify_commission: bool


class GetMembershipPackageCategoryResponse(Root):
    body: list[MembershipPackageCategory]

    class ApiProperties:
        paginated = False
        sortable = False
