from . import is_json
import json
from typing import Generic, TypeVar
from requests import JSONDecodeError
from requests_ratelimiter import LimiterSession
from api_client.utils.api_response import ApiResponse
from api_client.models.base import Root

burp = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}


ReturnModelType = TypeVar("ReturnModelType", bound=Root)
class Requester(Generic[ReturnModelType]):
    '''
    A Requester class to prepare and make API Requests with the given data
    '''
    default_header = {
        "Content-Type": "application/json",
        "User-Agent": "ANet APIClient v0.0.1"   
    }

    default_page_info = {
        "page_number": 1,
        "total_records_per_page": 1
    }

    def __init__(self, method: str, session: LimiterSession, endpoint: str, params: dict, ret_model: Root, post_body: dict = None) -> None:
        self.method = method
        self.session = session
        self.endpoint = endpoint
        self.params = params
        self.ret_model = ret_model
        self.headers = self.default_header.copy()
        self.post_body = post_body
        
        if self.ret_model.APIProperties.paginated:
            self.headers['page_info'] = self.default_page_info.copy()

    def prep_headers(self):
        headers = self.headers.copy()
        if headers.get('page_info', None):
            headers['page_info'] = json.dumps(headers['page_info'])
        return headers

    def __call__(self):
        headers = self.prep_headers()
        
        response = self.session.request(self.method, self.endpoint, params=self.params, headers=headers, json=self.post_body,  verify=False)
        print(response.request.path_url)
        print(response.request.url)
        # if for some reason the result is not Json try 10 more times to get JSON before returning None
        counter = 0
        while not is_json(response.content):
            response = self.session.request(self.method, self.endpoint, params=self.params, headers=headers, json=self.post_body, proxies=burp)
            counter += 1; 
            if counter > 10: return None
        
        # If we really do not have JSON now then return None
        try:
            json_data = response.json()
        except JSONDecodeError:
            return None
        
        # Convert returned data to pydantic model class and return it
        obj_data = self.ret_model(**json_data)
        return ApiResponse(self, obj_data)
    
    def get_next_page(self):
        if self.headers.get('page_info', None):
            self.headers['page_info']['page_number'] += 1
            return self()
        else:
            raise Exception("Unable to get next page for a non paginated API")
    