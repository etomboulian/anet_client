from api_client.models.base import Root, Body


class MembershipUsage(Body):
    customer_id: int
    customer_first_name: str
    customer_last_name: str
    package_id: int
    package_name: str
    pass_number: str
    alternate_key_type: str
    alternate_key_status: str
    alternate_key_id: str
    checkin_date: str
    checkin_day_of: str
    checkin_time: str
    qty: int
    check_in_entry_point_id: int
    checkin_entry_point: str
    checkout_date: str
    checkout_day_of: str
    checkout_time: str
    check_out_entry_point_id: int
    checkout_entry_point: str


class GetMembershipUsagesResponse(Root):
    body: list[MembershipUsage]

    class ApiProperties:
        paginated = True
        sortable = False
