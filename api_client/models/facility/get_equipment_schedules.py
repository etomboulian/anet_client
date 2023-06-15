from api_client.models.base import Root, Body


class EquipmentScheduleEntry(Body):
    equipment_id: int
    equipment_name: str
    equipment_type: str
    equipment_type_id: int
    equipment_number: str
    quantity: int
    setup_from_time: str
    setup_to_time: str
    booking_start_date_time: str
    booking_end_date_time: str
    tear_down_from_time: str | None
    tear_down_to_time: str | None
    schedule_id: int


class GetEquipmentSchedulesResponse(Root):
    body: list[EquipmentScheduleEntry]
