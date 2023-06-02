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

equipment = client.get_equipment(10); print(f"[t+{time.time()-start:.2f}] -> {equipment.response_object}"); input()
sitelist = client.get_sites() ; print(f"[t+{time.time()-start:.2f}] -> {sitelist.response_object}"); input()
org_data = client.get_organization() ; print(f"[t+{time.time()-start:.2f}] -> {org_data.response_object}"); input()
season_data = client.get_seasons(); print(f"[t+{time.time()-start:.2f}] -> {season_data.response_object}"); input()
skills_data = client.get_skills(); print(f"[t+{time.time()-start:.2f}] -> {skills_data.response_object}"); input()
centers_data = client.get_centers(); print(f"[t+{time.time()-start:.2f}] -> {centers_data.response_object}"); input()
memberships_data = client.get_memberships(); print(f"[t+{time.time()-start:.2f}] -> {memberships_data.response_object}"); input()


for i in range(1000):
    print(f"[t+{time.time()-start:.2f}] -> {client.get_sites().response_object}")
