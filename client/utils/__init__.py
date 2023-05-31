import json

def is_json(text: str):
    '''
    param: text (str) -> a string to check for the presence of a string that is convertible to JSON
    '''
    try:
        json.loads(text)
    except ValueError as e:
        return False
    return True


from .http_verbs import HttpVerbs
from .requester import Requester
from .url_builder import UrlBuilder
from .api_response import ApiResponse
from .api_info import ApiInfo