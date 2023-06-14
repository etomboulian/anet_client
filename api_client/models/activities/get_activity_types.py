from api_client.models.base import Root, Body


class ActivityType(Body):
    activity_type_id: int
    activity_type_name: str
    prevent_further_use: bool
    show_on_member_app: str


class GetActivityTypesResponse(Root):
    body: list[ActivityType]
    
    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "activitytypes"