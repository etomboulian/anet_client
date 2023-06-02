import time
from typing import Generic, TypeVar
from requests import JSONDecodeError
from requests_ratelimiter import LimiterSession

from . import is_json
from client.utils.api_response import ApiResponse
from client.models.base import Root


ReturnModelType = TypeVar("ReturnModelType", bound=Root)
class Requester(Generic[ReturnModelType]):
    '''
    A Requester class to prepare and make API Requests with the given data
    '''
    default_header = {
        "page_number" : "1",
        "total_records_per_page": "50"
    }

    def __init__(self, method: str, session: LimiterSession, endpoint: str, params: dict, ret_model) -> None:
        self.method = method
        self.session = session
        self.endpoint = endpoint
        self.params = params
        self.ret_model = ret_model
        self.page_info = self.default_header.copy()
        self.paginated = ret_model.ApiProperties.paginated

    def request(self):
        data = self.session.request(self.method, self.endpoint, params=self.params, headers=self.page_info)
        # print(data.url)
        # if for some reason the result is not Json try 10 more times to get JSON before returning None
        counter = 0
        while not is_json(data.content):
            data = self.session.request(self.method, self.endpoint, params=self.params, headers=self.page_info)
            counter += 1; 
            if counter > 10: return None
        
        # If we really do not have JSON now then return None
        try:
            json_data = data.json()
        except JSONDecodeError:
            return None

        # Convert returned data to pydantic model class and return it
        obj_data = self.ret_model(**json_data)
        return ApiResponse(self, obj_data)
    
    def request_next_page(self):
        if not self.paginated:
            raise Exception("Unable to get next page for a non paginated API")
        
        self.page_info["page_number"] += 1
        return self.request()
    