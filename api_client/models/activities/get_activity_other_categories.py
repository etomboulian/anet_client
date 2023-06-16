from api_client.models.base import Root, Body, ResponseTypes


class ActivityOtherCategory(Body):
    other_category_name: str
    other_category_id: int
    link_interest_list: bool
    hide_on_internet: bool


class GetActivityOtherCategoriesResponse(Root):
    body: list[ActivityOtherCategory]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "activityothercategories"
        response_type = ResponseTypes.LIST
