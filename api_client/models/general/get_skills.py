from api_client.models.base import Body, Root, ResponseTypes


class Skill(Body):
    skill_id: int
    skill_title: str
    skill_description: str
    available_for: str


class GetSkillsResponse(Root):
    body: list[Skill]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "skills"
        response_type = ResponseTypes.LIST