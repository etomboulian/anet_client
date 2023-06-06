import os
import dotenv
from unittest import TestCase
from api_client import SystemApiClient
from api_client.models.general.get_organization import GetOrganizationResponse, Organization


dotenv.load_dotenv()

# Entry = ("field_name", [*valid_types])
body_fields = (
    ("organization_id", [int]),
    ("name", [str]),
    ("time_zone", [str, None]),
    ("logo_on_member_app", [str]),
    ("country", [str]),
    ("retired", [str]),
    ("cui_url", [str])
)

sample_data = {
    "headers": {
        "response_code":"0000",
        "response_message":"Successful"
        },
    "body":[{
        "organization_id":1099,
        "name":"City of Vancouver",
        "time_zone":"US/Mountain",
        "logo_on_member_app":"",
        "country":"United States of America",
        "retired":"N",
        "cui_url":"http://apm.activecommunities.com/ljsupport12/Home"
        }]
    }

class TestGetOrganization(TestCase):
    def setUp(self) -> None:
        self.api_client = SystemApiClient(
            os.environ.get('ORG_NAME', 'ljsupport12'),
            os.environ.get('COUNTRY', 'USA'),
            os.environ.get('API_KEY', None),
            os.environ.get('API_SECRET', None)
        )
        self.data = self.api_client.get_organization().data
        return super().setUp()
    
    def test_response_successful(self):
        self.assertEqual(self.data.headers.response_code, "0000")
        self.assertEqual(self.data.headers.response_message, "Successful")

    def test_correct_response_type(self):
        self.assertIsInstance(self.data, GetOrganizationResponse, 
                              f"GetOrganization API returned a response of the wrong type - {type(self.data)}")
        
        self.assertIsInstance(self.data.body, list)

        self.assertIsInstance(self.data.body[0], Organization, 
                              f"GetOrganization API returned a response body of the wrong type - {type(self.data.body[0])}")

    def test_correct_response_fields(self):
        for field_name, types in body_fields:
            data = getattr(self.data.body[0], field_name, None)
            self.assertIsNotNone(data, f"Organization object received an unexpected field: {field_name}")
            self.assertTrue(type(data) in types, f"Organization object field -> {field_name} received unexpected type of {type(data)} expected {types}")
            
    def test_api_response_deserialization(self):
        response_obj = GetOrganizationResponse(**sample_data)
        self.assertIsInstance(response_obj, GetOrganizationResponse)
        self.assertIsInstance(response_obj.body, list)
        self.assertIsInstance(response_obj.body[0], Organization)
