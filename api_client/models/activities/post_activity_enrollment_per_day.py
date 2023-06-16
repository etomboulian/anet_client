from api_client.models.base import Root, Body, ResponseTypes


class ActivityEnrollmentDate(Body):
    reservation_id: int


class PostActivityEnrollmentPerDayResponse(Root):
    body: list[ActivityEnrollmentDate]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "activityenrollmentperday"
        response_type = ResponseTypes.SINGLE
        