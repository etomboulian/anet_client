from api_client.models.base import Root, Body, ResponseTypes
from datetime import datetime



class MultipleChoiceAnswer(Body):
    default_response: bool
    answer_code: str | None
    answer: str | None
    sub_question: int | None
    demographic: str | None


class AutoFillConditionalAnswer(Body):
    answer: str
    age_from: int
    age_to: int
    gender: str


class CustomQuestion(Body):
    custom_question_id: int
    modified_date_time: datetime
    custom_question_title: str
    prevent_further_use: bool
    custom_question_text: str
    display: str
    answer_type: str
    answer_required: bool
    use_answer_code: bool
    answer_format: str | None
    maximum_length: int
    default_answer: str | None
    question_scope: str
    multiple_choice_answers: list[MultipleChoiceAnswer]
    auto_fill_conditional_answers: list[AutoFillConditionalAnswer]


class GetCustomQuestionsResponse(Root):
    body: list[CustomQuestion]

    class APIProperties:
       paginated = False
       sortable = False
       endpoint = 'customquestions'
       response_type = ResponseTypes.LIST
