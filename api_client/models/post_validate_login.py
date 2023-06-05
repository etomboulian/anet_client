from pydantic import BaseModel
from .base import Root, Body

class Headers(Body):
    response_code: str
    response_message: str


class LoginInformation(Body):
    customer_title: str | None
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    gender: str | None
    birth_date: str | None
    age_category: str | None
    customer_id: int
    encrypted_customer_id: str


class PostValidateLoginResponse(Root):
    body: list[Body]

    class ApiProperties:
        paginated = False
        sortable = False
