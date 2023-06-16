from typing import TypeVar, Generic

from api_client.models.base import Root, PageInfo

ReturnModelType = TypeVar("ReturnModelType", bound=Root)
class ApiResponse(Generic[ReturnModelType]):
    def __init__(self, requester, response_object: ReturnModelType) -> None:
        self.data = response_object
        self.headers = response_object.headers
        self.body = response_object.body
        self.requester = requester

    def request_next_page(self):
        pass
    
    # Call next pages using the iterator pattern
    def __iter__(self):
        return self.data
    
    def __next__(self):
        return self.requester.request_next_page()
    