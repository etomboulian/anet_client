import os
from client import SystemApiClient as ApiClient
from dotenv import load_dotenv

load_dotenv()

org_name = os.environ.get('ORG_NAME') 
country = os.environ.get('COUNTRY')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

client = ApiClient(org_name, country, api_key, api_secret)


import time
start = time.time()

equipment = client.get_equipment(10); print(f"[t+{time.time()-start:.2f}] -> {equipment.data_model}")
sitelist = client.get_sites() ; print(f"[t+{time.time()-start:.2f}] -> {sitelist.data_model}")
org_data = client.get_organization() ; print(f"[t+{time.time()-start:.2f}] -> {org_data.data_model}")

for i in range(1000):
    print(f"[t+{time.time()-start:.2f}] -> {client.get_sites().data_model}")
