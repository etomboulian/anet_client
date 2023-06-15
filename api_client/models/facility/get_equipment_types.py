from api_client.models.base import Root, Body


class EquipmentType(Body):
    description: str
    equipment_type_id: int
    show_on_member_app: str
    prevent_further_use: bool
    bookable_lendable: str


class GetEquipmentTypesResponse(Root):
    body: list[EquipmentType]

    class ApiProperties:
        paginated = False
        sorted = False
        endpoint = "equipmenttypes"
