
from api_client.models.base import Root


class PostForgotPasswordResponse(Root):
    body: list

    class ApiProperties:
        paginated = False
        sortable = False
