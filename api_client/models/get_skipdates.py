from pydantic import BaseModel
from api_client.models.base import Body, Root


class Headers(BaseModel):
    response_code: str
    response_message: str


class SkipDate(Body):
    skip_date_description: str
    skip_every_year: bool
    date_from: str
    time_from: str
    date_to: str
    time_to: str


class GetSkipDatesResponse(Root):
    headers: Headers
    body: list[SkipDate]
    
    class ApiProperties:
        paginated = True
        sortable = True