from hashlib import sha256
import time

VALID_COUNTRIES = ("USA", "CAN")

class ApiInfo:
    def __init__(self, org_name: str, country: str, api_key: str, secret: str) -> None:
        self.org_name = org_name
        self.country = country
        self.api_key = api_key
        self.secret = secret
        self.default_page_size = 50

        if not self._check_country(self.country):
            raise ValueError(f"Country must be one of {VALID_COUNTRIES[0]} or {VALID_COUNTRIES[1]}")
    
    def _check_country(self, country_name):
        return country_name in VALID_COUNTRIES
    
    def _extract_args(self, arg_dict):
        request_args = {}
        if arg_dict is not None:
            request_args = arg_dict.copy()
            request_args.pop("self")
            request_args = { k:v for (k,v) in request_args.items() if v is not None }
        return request_args
    
    def _generate_signature(self):
        value = self.api_key + self.secret + str(int(time.time()))
        return sha256(value.encode()).hexdigest()
    
    # Default params will consist of [non empty api function parameters] + api_key + sig
    def _create_default_params(self, arg_dict):
        request_params = self._extract_args(arg_dict)
        request_params['api_key'] = self.api_key
        request_params['sig'] = self._generate_signature()
        return request_params
