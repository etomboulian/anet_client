from api_client.models.base import Root, Body


class InstructorScheduleEntry(Body):
    instructor_id: int
    instructor_first_name: str
    instructor_last_name: str
    instructor_email: str
    instructor_schedule_type: str
    schedule_start: str
    schedule_end: str
    activity_name: str
    activity_number: str
    activity_id: int
    facility_id: int
    facility_name: str
    customer_first_name: str
    customer_last_name: str
    customer_id: int
    permit_number: str
    event_name: str


class GetInstructorSchedulesResponse(Root):
    body: list[InstructorScheduleEntry]

    class ApiProperties:
        paginated = True
        sortable = False
        endpoint = "instructorschedules" 
