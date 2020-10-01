#retriving test_database collection data

from pymongo import MongoClient
client=MongoClient()

mydb=client['test_database']
coll_list=mydb.list_collection_names()
print('Collections available in test_database are: ', coll_list)

api_users=mydb['api_users']
client_user=mydb['client_user']
roles=mydb['roles']
permissions=mydb['permissions']
routes= mydb['routes']
cost_centers=mydb['cost_centers']
    

#filename is collection name in mongodb
def test_db_data(file_name):
    coll_data=[i for i in file_name.find()]
    return coll_data

test_db_data(api_users)