from api_client.models.base import Root, Body


class ActivityDropInPayment(Body):
    dropin_fee: int
    convenience_fee: int
    convenience_fee_discount: float
    tax: int
    iframe_url: str


class PostActivityDropInPaymentResponse(Root):
    body: list[ActivityDropInPayment]

    class ApiProperties:
        paginated = False
        sortable = False
        endpoint = "activitydropinpayment"