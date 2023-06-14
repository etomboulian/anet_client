from api_client.models.base import Root

class DeleteActivityEnrollmentPerDayResponse(Root):
    body: list

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "activityenrollmentperday"