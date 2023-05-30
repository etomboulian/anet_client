from client import SystemApiClient as ApiClient
from dotenv import load_dotenv
import os

load_dotenv()


org_name = os.environ.get('ORG_NAME') 
country = os.environ.get('COUNTRY')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

client = ApiClient(org_name, country, api_key, api_secret)

equipment = client.get_equipment(10)
site = client.get_sites()
print(site.data_model)
