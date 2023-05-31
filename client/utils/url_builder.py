
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