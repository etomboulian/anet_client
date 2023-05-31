from pydantic import BaseModel
from base import Body, Root


class ChildSeason(BaseModel):
    child_season_id: int
    child_season: str
    start_date: str
    end_date: str
    prevent_further_use: bool
    first_date_in_person: str
    first_date_in_person_non_residents: str
    first_date_in_person_members: str
    last_date_in_person: str
    first_date_on_internet: str
    first_date_on_internet_non_residents: str
    first_date_on_internet_members: str
    last_date_on_internet: str


class Season(Body):
    season_id: int
    season_name: str
    child_season: list[ChildSeason]
    start_date: str
    end_date: str
    site_id: int
    prevent_further_use: bool
    first_date_in_person: str
    first_date_in_person_non_residents: str
    first_date_in_person_members: str
    last_date_in_person: str
    first_date_on_internet: str
    first_date_on_internet_non_residents: str
    first_date_on_internet_members: str
    last_date_on_internet: str


class GetSeasonsResponse(Root):
    body: list[Season]
