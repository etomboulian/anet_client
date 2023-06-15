from api_client.models.base import Root, Body
from datetime import time

class Headers(Body):
    response_code: str
    response_message: str


class PrepCode(Body):
    description: str
    prep_code_id: int
    site_name: str | None
    setup_time: int
    teardown_time: int
    notes: str


class GetPrepCodesResponse(Root):
    headers: Headers
    body: list[PrepCode]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "prepcodes"


