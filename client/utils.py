from typing import Generic, TypeVar
from requests_ratelimiter import LimiterSession
from client.models.base import Root


ReturnModelType = TypeVar("ReturnModelType")
class SinglePageAPIRequester(Generic[ReturnModelType]):
    def __init__(self, request_result: dict, return_model: ReturnModelType):
        self.data = return_model(**request_result)
        print(self.data)


class PaginatedAPI(Generic[ReturnModelType]):
    paginated = True
    default_header = {
        "page_number" : "1",
        "total_records_per_page": "50"
    }

    def __init__(self, session: LimiterSession, endpoint: str, params: dict, ret_model: ReturnModelType) -> None:
        self.session = session
        self.endpoint = endpoint
        self.params = params
        self.ret_model = ret_model
        self.page_info = self.default_header.copy()

    def request(self):
        print(self.endpoint)
        data = self.session.get(self.endpoint, params=self.params, headers=self.page_info)
        data.raise_for_status()
        json_data = data.json()
        obj_data = self.ret_model(**json_data)
        return PaginatedAPIResult(obj_data)
    
    
class PaginatedAPIResult:
    def __init__(self, data_model: Root) -> None:
        self.data_model = data_model    


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