from pydantic import BaseModel

from client.models.base import Body, Root


class Skill(Body):
    skill_id: int
    skill_title: str
    skill_description: str
    available_for: str


class GetSkillsResponse(Root):
    body: list[Skill]
