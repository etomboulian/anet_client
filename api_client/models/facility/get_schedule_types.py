from api_client.models.base import Root, Body


class ScheduleType(Body):
    schedule_type_id: int
    description: str
    site_id: int
    site_name: str
    type_code: str | None
    booking_assignment: str | None
    apply_reservation_charge: bool
    auto_complete_if_no_charge: bool
    hide_notes_section: bool
    hide_disclaimer_section: bool
    hide_checklist_section: bool
    hide_approval_stages_section: bool
    hide_custom_questions_section: bool
    default_customer: str


class GetScheduleTypesResponse(Root):
    body: list[ScheduleType]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "scheduletypes"