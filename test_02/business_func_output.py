
import business
from pymongo import MongoClient
client=MongoClient()

mydb=client['test_database']
api_users=mydb['api_users']
client_user=mydb['client_user']

b= client_user.find({})
list_dep_id=[]
for x in b:
    #print(x['departament_id'])
    list_dep_id.append(x['departament_id'])
  
print(list_dep_id[0])
business.get_unpaginated_client_users(list_dep_id[0])