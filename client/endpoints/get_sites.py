# This function will get attached to the main SystemApiClient object 
# The SystemApiClient object will then be self
from client.api_client import PaginatedAPI
from client.models.sites import SitesResult


def get_sites(self):

    params = self.extract_args(locals())
    params['api_key'] = self.api_key
    params['sig'] = self.generate_signature()
    
    endpoint = self.url.get_endpoint('sites')  

    return PaginatedAPI(self.session, endpoint, params, SitesResult).request()
