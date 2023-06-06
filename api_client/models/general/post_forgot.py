from api_client.models.base import Root


class PostForgotResponse(Root):
    body: list

    class ApiProperties:
        paginated = False
        sortable = False
