from api_client.models.base import Root, Body
from datetime import datetime

class QuestionAnswer(Body):
    question: str
    question_id: int
    answer: str | None
    time_stamp: datetime | None


class CustomQuestionAnswer(Body):
    customer_id: int
    first_name: str
    last_name: str
    question_answers: list[QuestionAnswer]
    answer_for: str
    receipt_number: float
    activity_name: str | None
    activity_number: str | None
    activity_id: int | None
    activity_status: str | None
    program_name: str | None
    program_number: str | None
    program_id: int | None
    program_status: str | None
    event_type: str | None
    event_name: str | None
    permit_number: str | None
    permit_status: str | None
    package_name: str | None
    package_id: int | None


class GetCustomQuestionAnswerResponse(Root):
    body: list[CustomQuestionAnswer]

    class ApiProperties:
       paginated = False
       sortable = False
