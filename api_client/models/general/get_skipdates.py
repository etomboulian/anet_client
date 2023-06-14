from api_client.models.base import Body, Root


class SkipDate(Body):
    skip_date_description: str
    skip_every_year: bool
    date_from: str
    time_from: str
    date_to: str
    time_to: str


class GetSkipDatesResponse(Root):
    body: list[SkipDate]
    
    class ApiProperties:
        paginated = True
        sortable = True
        endpoint = "skipdates"