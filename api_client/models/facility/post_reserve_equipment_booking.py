from api_client.models.base import Root, Body, ResponseTypes


class ReserveEquipmentBooking(Body):
    schedule_id: int
    transaction_id: int


class PostReserveEquipmentBookingResponse(Root):
    body: list[ReserveEquipmentBooking]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "reserveequipmentbooking"
        response_type = ResponseTypes.SINGLE
        