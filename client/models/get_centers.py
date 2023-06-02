from client.models.base import Root, Body
from datetime import time


class DefaultHoursOfOperation(Body):
    default_opens: time | None
    default_closes: time | None


class SundayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class MondayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class TuesdayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class WednesdayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class ThursdayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class FridayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class SaturdayHoursOfOperation(Body):
    closed_all_day: bool
    opens: time | None
    closes: time | None


class Center(Body):
    center_id: int
    center_name: str
    prevent_further_use: bool
    site_id: int
    site_name: str
    show_on_member_app: str
    member_app_image: str
    latitude: str
    longitude: str
    description: str
    customer_webpage_url: str
    address1: str
    address2: str
    city: str
    state: str
    zip_code: str
    country: str
    phone1: str
    phone2: str
    fax: str
    default_hours_of_operation: DefaultHoursOfOperation
    Sunday_hours_of_operation: SundayHoursOfOperation
    Monday_hours_of_operation: MondayHoursOfOperation
    Tuesday_hours_of_operation: TuesdayHoursOfOperation
    Wednesday_hours_of_operation: WednesdayHoursOfOperation
    Thursday_hours_of_operation: ThursdayHoursOfOperation
    Friday_hours_of_operation: FridayHoursOfOperation
    Saturday_hours_of_operation: SaturdayHoursOfOperation


class GetCentersResponse(Root):
    body: list[Center]
    
    class ApiProperties:
        paginated = False
        sortable = False
