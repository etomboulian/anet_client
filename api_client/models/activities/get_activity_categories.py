from api_client.models.base import Root, Body, ResponseTypes


class ActivityCategory(Body):
    activity_category_name: str
    category_id: int
    link_interest_list: bool
    hide_on_internet: bool
    show_on_member_app: str


class GetActivityCategoriesResponse(Root):
    body: list[ActivityCategory]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "activitycategories"
        response_type = ResponseTypes.LIST
