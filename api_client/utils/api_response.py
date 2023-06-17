from typing import TypeVar, Generic

from api_client.models.base import Root, PageInfo, ResponseTypes


ReturnModelType = TypeVar("ReturnModelType", bound=Root)
class ApiResponse(Generic[ReturnModelType]):
    def __init__(self, requester, response_object: ReturnModelType) -> None:
        self.response = response_object
        self.requester = requester
        self.data = self.response.body

    @property
    def data(self):
        match self.response.APIProperties.response_type:
            case ResponseTypes.NONE:
                return None
            case ResponseTypes.SINGLE:
                return self._data[0]
            case ResponseTypes.LIST:
                return self._data
    
    @data.setter
    def data(self, val):
        self._data = val


    def get_next_page(self):
        return self.requester.get_next_page()