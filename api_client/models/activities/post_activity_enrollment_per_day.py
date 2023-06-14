from api_client.models.base import Root, Body


class ActivityEnrollmentDate(Body):
    reservation_id: int


class PostActivityEnrollmentPerDayResponse(Root):
    body: list[ActivityEnrollmentDate]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "activityenrollmentperday"
        