from api_client.models.base import Root, Body
from datetime import date

class Family(Body):
    family_id: int


class FamilyMember(Body):
    customer_id: int
    encrypted_customer_id: str
    first_name: str
    last_name: str
    customer_type: str | None
    birth_date: date | None
    age_category: str | None
    gender: str
    age: str
    date_time_modified: str
    retired_status: str | None
    families: list[Family]


class GetFamilyMembersResponse(Root):
    body: list[FamilyMember]

    class ApiProperties:
       paginated = False
       sortable = False
       endpoint = "familymembers"