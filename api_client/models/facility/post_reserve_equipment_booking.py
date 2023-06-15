from api_client.models.base import Root, Body


class ReserveEquipmentBooking(Body):
    schedule_id: int
    transaction_id: int


class PostReserveEquipmentBookingResponse(Root):
    body: list[ReserveEquipmentBooking]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "reserveequipmentbooking"
        