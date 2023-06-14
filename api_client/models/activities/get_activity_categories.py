from api_client.models.base import Root, Body


class ActivityCategory(Body):
    activity_category_name: str
    category_id: int
    link_interest_list: bool
    hide_on_internet: bool
    show_on_member_app: str


class GetActivityCategoriesResponse(Root):
    body: list[ActivityCategory]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "activitycategories"
