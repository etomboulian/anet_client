from api_client.models.base import Root, Body, ResponseTypes


class Refund(Body):
    receipt_date: str
    receipt_time: str
    payee_company_name: str
    payee_company_id: int
    payee_customer_name: str
    payee_customer_id: int
    payee_home_phone: str | None
    payee_work_phone: str | None
    payee_cell_phone: str | None
    payee_other_phone: str | None
    payee_residential_address1: str | None
    payee_residential_address2: str | None
    payee_residential_city: str | None
    payee_residential_state_or_province: str | None
    payee_residential_zip_code: str | None
    payee_mailing_address1: str | None
    payee_mailing_address2: str | None
    payee_mailing_city: str | None
    payee_mailing_state_or_province: str | None
    payee_mailing_zip_code: str | None
    original_receipt_number: int
    receipt_number: int
    payment_type: str
    payment_type_id: int
    refund_detail: str
    refund_amount: int
    gl_account_number_refund_from: str
    gl_account_name_refund_from: str
    gl_account_number_refund_to: str
    gl_account_name_refund_to: str
    transaction_site_id: int
    transaction_site: str


class GetRefundsResponse(Root):
    body: list[Refund]

    class APIProperties:
        paginated = True
        sortable = True
        endpoint = "refunds"
        response_type = ResponseTypes.LIST
