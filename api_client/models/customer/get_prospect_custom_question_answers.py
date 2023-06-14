from api_client.models.base import Root, Body


class ProspectAnswer(Body):
    question: str
    answer: list[str]


class ProspectCustomQuestionAnswers(Body):
    customer_id: int
    prospect_answers: list[ProspectAnswer]


class GetProspectCustomQuestionAnswersResponse(Root):
    body: list[ProspectCustomQuestionAnswers]

    class ApiProperties:
       paginated = False
       sortable = False