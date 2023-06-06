import time
import json
from typing import Generic, TypeVar
from requests import JSONDecodeError
from requests_ratelimiter import LimiterSession

from . import is_json
from api_client.utils.api_response import ApiResponse
from api_client.models.base import Root


ReturnModelType = TypeVar("ReturnModelType", bound=Root)
class Requester(Generic[ReturnModelType]):
    '''
    A Requester class to prepare and make API Requests with the given data
    '''
    default_header = {
        "Content-Type": "application/json",
        #"User-Agent": "ANet-APIClient-v0.0.1",
        #"page_info": json.dumps({
        #    "page_number" : "1",
        #    "total_records_per_page": "50"
        #})
    }

    def __init__(self, method: str, session: LimiterSession, endpoint: str, params: dict, ret_model, post_body: dict = None) -> None:
        self.method = method
        self.session = session
        self.endpoint = endpoint
        self.params = params
        self.ret_model = ret_model
        self.page_info = self.default_header.copy()
        self.paginated = ret_model.ApiProperties.paginated
        self.post_body = post_body

    def __call__(self):
        data = self.session.request(self.method, self.endpoint, params=self.params, headers=self.page_info, json=self.post_body)
        
        # if for some reason the result is not Json try 10 more times to get JSON before returning None
        counter = 0
        while not is_json(data.content):
            data = self.session.request(self.method, self.endpoint, params=self.params, headers=self.page_info, json=self.post_body)
            counter += 1; 
            if counter > 10: return None
        
        # If we really do not have JSON now then return None
        try:
            json_data = data.json()
        except JSONDecodeError:
            return None
        #print(json_data)
        # Convert returned data to pydantic model class and return it
        obj_data = self.ret_model(**json_data)
        return ApiResponse(self, obj_data)
    
    def request_next_page(self):
        if not self.paginated:
            raise Exception("Unable to get next page for a non paginated API")
        
        self.page_info["page_number"] += 1
        return self.request()
    