from typing import TypeVar
from client.api_client import SystemApiClient


from client.models.base import Root, PageInfo
from .requester import Requester

ReturnModelType = TypeVar("ReturnModelType", bound=Root)
class ApiResponse:
    def __init__(self, requester: Requester, response_object: ReturnModelType) -> None:
        self.headers = response_object.headers
        self.data = response_object.body
        self.requester = requester
    
    # Call next pages using the iterator pattern
    def __iter__(self):
        return self.data
    
    def __next__(self):
        return self.requester.request_next_page()
    