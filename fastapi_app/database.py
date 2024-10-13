# database.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["fastapi_db"]


items_collection = db["items"]
clockin_collection = db["user_clockin_records"]




