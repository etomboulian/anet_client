from datetime import date, datetime
from requests_ratelimiter import LimiterSession
from client.api_client import PaginatedAPI
from client.models.equipment import EquipmentResult


# This function will get attached to the main SystemApiClient object 
# The SystemApiClient object will then be self
def get_equipment( 
    self,
    equipment_id: int = None,
    center_ids: str = None,
    bookable_or_lendable: int = None,
    modified_date_from: date = None,
    modified_date_to: date = None,
    show_on_member_app: bool = None,
    open_block_date_from: date = None,
    ):
    '''
    ** Note: At least one of the following parameters must be provided: 
    'equipment_id', 'center_ids', 'modified_date_from' and 'modified_date_to'.

    Has Params:      True
    Is Paginated:    True
    Allows Sorting:  False

    Retrieves an object representing the request to the Active Net Get Equipment API Endpoint

    param: equipment_id | string
        - The ID of the equipment item
    
    param: center_ids | string
        - You can specify up to 5 center IDs, with each center ID separated by a comma.

    param: bookable_or_lendable | int
        - Filter for equipment by their Bookable or Lendable property: 0-Both; 1-Bookable; 2-Lendable
    '''
    # Check that at least one required parameter is included
    if not equipment_id or center_ids or modified_date_from and modified_date_to:
        raise ValueError('At least one of the following parameters must be provided: equipment_id, center_ids, modified_date_from and modified_date_to.')

    # Build the params
    params = self.extract_args(locals())
    params['api_key'] = self.api_key
    params['sig'] = self.generate_signature()

    # Build the endpoint
    endpoint = self.url.get_endpoint('equipment')       
    
    return print(PaginatedAPI(self.session, endpoint, params, EquipmentResult).request())

        