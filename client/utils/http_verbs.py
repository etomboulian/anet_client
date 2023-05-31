from enum import Enum


class HttpVerbs(str, Enum):
    get = "GET"
    post = 'POST'
    put = 'PUT'
    delete = 'DELETE'