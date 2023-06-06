import os
from api_client import SystemApiClient as ApiClient
from dotenv import load_dotenv

load_dotenv()

org_name = os.environ.get('ORG_NAME') 
country = os.environ.get('COUNTRY')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

client = ApiClient(org_name, country, api_key, api_secret)


import time
start = time.time()

#equipment = client.get_equipment(10); print(f"[t+{time.time()-start:.2f}] -> {equipment.data}"); input()
#sitelist = client.get_sites() ; print(f"[t+{time.time()-start:.2f}] -> {sitelist.data}"); input()
#org_data = client.get_organization() ; print(f"[t+{time.time()-start:.2f}] -> {org_data.data}"); input()
#season_data = client.get_seasons(); print(f"[t+{time.time()-start:.2f}] -> {season_data.data}"); input()
#skills_data = client.get_skills(); print(f"[t+{time.time()-start:.2f}] -> {skills_data.data}"); input()
#centers_data = client.get_centers(); print(f"[t+{time.time()-start:.2f}] -> {centers_data.data}"); input()
#memberships_data = client.get_memberships(); print(f"[t+{time.time()-start:.2f}] -> {memberships_data.data}"); input()
#login_result = client.post_validate_login('evan.tomboulian@activenetwork.com', 'Password@1'); print(f"[t+{time.time()-start:.2f}] -> {login_result.data}"); input()
#forgot_password = client.post_forgot_password('etomboulian@gmail.com'); print(f"[t+{time.time()-start:.2f}] -> {forgot_password.data}"); input()
#activities = client.get_activities(); print(f"[t+{time.time()-start:.2f}] -> {activities.data}"); input()
#activity_detail = client.get_activity_detail(100); print(f"[t+{time.time()-start:.2f}] -> {activity_detail.data}"); input()
#categories = client.get_activity_categories(); print(f"[t+{time.time()-start:.2f}] -> {categories.data}"); input()
#other_cat = client.get_activity_other_categories(); print(f"[t+{time.time()-start:.2f}] -> {other_cat.data}"); input()
#act_fees = client.get_activity_fees(100); print(f"[t+{time.time()-start:.2f}] -> {act_fees.data}"); input()
#act_types = client.get_activity_types(); print(f"[t+{time.time()-start:.2f}] -> {act_types.data}"); input()
#act_enr = client.get_activity_enrollment(activity_id=110); print(f"[t+{time.time()-start:.2f}] -> {act_enr.data}"); input()
exp_detail = client.get_activity_expanded_detail(10); print(f"[t+{time.time()-start:.2f}] -> {exp_detail.data}"); input()
#for i in range(1000):
#    print(f"[t+{time.time()-start:.2f}] -> {client.get_sites().data}")
