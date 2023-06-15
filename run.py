import os, datetime
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
#exp_detail = client.get_activity_expanded_detail(10); print(f"[t+{time.time()-start:.2f}] -> {exp_detail.data}"); input()
#
#customers = client.get_customers(customer_ids='1,10,100'); print(f"[t+{time.time()-start:.2f}] -> {customers.data}"); input()
#cq = client.get_custom_questions(activity_id=101); print(f"[t+{time.time()-start:.2f}] -> {cq.data}"); input()
#cqa = client.get_custom_question_answers(activity_id=101); print(f"[t+{time.time()-start:.2f}] -> {cqa.data}"); input()
#pcq = client.get_prospect_custom_question_answers(customer_ids='100,10,1'); print(f"[t+{time.time()-start:.2f}] -> {pcq.data}"); input()
#fm = client.get_family_members(family_ids='1,2,3,4,5,6,7,8'); print(f"[t+{time.time()-start:.2f}] -> {fm.data}"); input()

fac = client.get_facilities(10); print(f"[t+{time.time()-start:.2f}] -> {fac.data}"); input()
fac_det = client.get_facility_details(10);print(f"[t+{time.time()-start:.2f}] -> {fac_det.data}"); input()
fac_type = client.get_facility_types(); print(f"[t+{time.time()-start:.2f}] -> {fac_type.data}"); input()
fac_sched = client.get_facility_schedules(datetime.date(2023,6,15), datetime.date(2023,8,30), '10,100,1'); print(f"[t+{time.time()-start:.2f}] -> {fac_sched.data}"); input()

event_types = client.get_event_types(); print(f"[t+{time.time()-start:.2f}] -> {event_types.data}"); input()
res_grp = client.get_reservation_groups(); print(f"[t+{time.time()-start:.2f}] -> {res_grp.data}"); input()
prep = client.get_prep_codes(); print(f"[t+{time.time()-start:.2f}] -> {prep.data}"); input()
#for i in range(1000):
#    print(f"[t+{time.time()-start:.2f}] -> {client.get_sites().data}")
