# database.py
from pymongo import MongoClient

client = MongoClient("mongodb+srv://anand:Troodonmg123@cluster0.kkt3f.mongodb.net/")
db = client["fastapi_db"]


items_collection = db["items"]
clockin_collection = db["user_clockin_records"]




