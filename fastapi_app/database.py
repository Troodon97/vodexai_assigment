# # database.py
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://anand:Troodonmg123@cluster0.kkt3f.mongodb.net/")
# db = client["fastapi_db"]


# items_collection = db["items"]
# clockin_collection = db["user_clockin_records"]



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://anand:Troodonmg123@cluster0.kkt3f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["fastapi_db"]


items_collection = db["items"]
clockin_collection = db["user_clockin_records"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)




