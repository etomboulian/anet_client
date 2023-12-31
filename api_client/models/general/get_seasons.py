from datetime import date, datetime
from api_client.models.base import Body, Root, ResponseTypes


class ChildSeason(Body):
    child_season_id: int
    child_season: str | None
    start_date: date | None
    end_date: date | None
    prevent_further_use: bool
    first_date_in_person: datetime | None
    first_date_in_person_non_residents: datetime | None
    first_date_in_person_members: datetime | None
    last_date_in_person: datetime | None
    first_date_on_internet: datetime | None
    first_date_on_internet_non_residents: datetime | None
    first_date_on_internet_members: datetime | None
    last_date_on_internet: datetime | None


class Season(Body):
    season_id: int
    season_name: str | None
    child_season: list[ChildSeason]
    start_date: date | None
    end_date: date | None
    site_id: int | None
    prevent_further_use: bool
    first_date_in_person: datetime | None
    first_date_in_person_non_residents: datetime | None
    first_date_in_person_members: datetime | None
    last_date_in_person: datetime | None
    first_date_on_internet: datetime | None
    first_date_on_internet_non_residents: datetime | None
    first_date_on_internet_members: datetime | None
    last_date_on_internet: datetime | None

    # class Config:
    #     json_encoders = {
    #         date: lambda x: datetime #.str | Noneptime(x, "%Y-%m-%d")
    #     }


class GetSeasonsResponse(Root):
    body: list[Season]

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "seasons"
        response_type = ResponseTypes.LIST
