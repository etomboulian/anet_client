from datetime import datetime
from api_client.models.base import Body, Root, ResponseTypes

class OpenBlock(Body):
    date: datetime
    time_block_on_date: str


class Equipment(Body):
    equipment_name: str
    equipment_id: int
    equipment_number: str
    equipment_type_id: int
    center_id: int
    status: int
    total_quantity: int
    default_setup: int
    default_cleanup: int
    show_on_member_app: str
    bookable_or_lendable: str
    open_blocks: list[OpenBlock]
    

class GetEquipmentResponse(Root):
    body: list[Equipment]

    class APIProperties:
        paginated = True
        sortable = False
        endpoint = 'equipment'
        response_type = ResponseTypes.LIST