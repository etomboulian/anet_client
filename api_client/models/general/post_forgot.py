from api_client.models.base import Root, ResponseTypes

# This model works for both the PostForgotPassword and PostForgotLoginName API Endpoints

class PostForgotResponse(Root):
    body: list

    class APIProperties:
        paginated = False
        sortable = False
        endpoint = "forgotpassword"
        response_type = ResponseTypes.NONE
