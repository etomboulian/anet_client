from pydantic import BaseModel


# Base Classes
class PageInfo(BaseModel):
    page_number: int
    total_records_per_page: int
    order_by: str
    order_option: str    # TODO: maybe enum for asc/desc?

class Headers(BaseModel):
    response_code: str
    response_message: str
    page_info: PageInfo | None

class Body (BaseModel):
    pass

class Root(BaseModel):
    headers: Headers
    body: list[Body]
