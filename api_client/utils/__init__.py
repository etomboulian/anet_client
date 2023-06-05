from enum import Enum
import json

def is_json(text: str) -> bool:
    '''
    param: text (str) -> a string to check for the presence of a string that is convertible to JSON
    '''
    try:
        json.loads(text)
    except ValueError as e:
        return False
    return True

def bool_to_str(condition: bool) -> str:
    if not type(condition) == bool:
        return ValueError('bool to str only accepts a boolean value')
    return "Y" if condition is True else "N"


class HttpVerbs(str, Enum):
    get = "GET"
    post = 'POST'
    put = 'PUT'
    delete = 'DELETE'


class UrlBuilder:
    host_address = "api.amp.active.com"
    service_name = {
        "USA": "anet-systemapi-sec",
        "CAN": "anet-systemapi-ca-sec"
    }

    def __init__(self, org_name, country) -> None:
        self.base_url = f"https://{self.host_address}/{self.service_name[country]}/{org_name}/api/v1/"

    def get_endpoint(self, endpoint: str):
        return self.base_url + endpoint + '/'


from .requester import Requester
from .api_response import ApiResponse
from .api_info import ApiInfo