# main.py
from fastapi import FastAPI, HTTPException
from pymongo import ReturnDocument
from bson import ObjectId
from datetime import datetime
from typing import List


from .database import items_collection, clockin_collection
from .schemas import Item, ItemUpdate, ClockIn, ClockInUpdate

app = FastAPI()

def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "item_name": item["item_name"],
        "quantity": item["quantity"],
        "expiry_date": item["expiry_date"].strftime("%Y-%m-%d"),  # Convert date to string
        "insert_date": item["insert_date"].strftime("%Y-%m-%d")
        
    
    }
    
def clock_helper(item)-> dict:
    return {

        "email": item['email'],
        "location": item['location'],
        "insert_date": item['insert_date'].strftime('%Y-%m-%d')
    }

@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    item_dict = dict(item)
    item_dict['insert_date'] = datetime.now()
    
    result = items_collection.insert_one(item_dict)
    return {"id": str(result.inserted_id)}

@app.get("/items/{id}")
async def get_item(id: str):
    item = items_collection.find_one({"_id": ObjectId(id)})

    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/filter/", response_model=List[dict])
async def filter_items(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": datetime.strptime(expiry_date, "%Y-%m-%d")}
    if insert_date:
        query["insert_date"] = {"$gt": datetime.strptime(insert_date, "%Y-%m-%d")}
    if quantity:
        query["quantity"] = {"$gte": quantity}
    
    print(query)
    items = items_collection.find(query)
    return [item_helper(item) for item in items]

@app.get("/items/aggregate_email/", response_model=List[dict])
async def aggregate_items_by_email():
    pipeline = [{"$group": {"_id": "$email", "count": {"$sum": 1}}}]
    result = list(items_collection.aggregate(pipeline))
    return [{"email": r["_id"], "count": r["count"]} for r in result]

@app.delete("/items/deltete/{id}", response_model=dict)
async def delete_item(id: str):
    result = items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/update/{id}", response_model=dict)
async def update_item(id: str, item: ItemUpdate):
    new_item = item.dict(exclude_unset=True) 
    updated_item = items_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": new_item},
        return_document=ReturnDocument.AFTER
    )
    if updated_item:
        return {'message':'Updated element'}
    raise HTTPException(status_code=404, detail="Item not found")

# ----------- crud for clock in records -----------
@app.post("/clock-in/", response_model=dict)
async def clock_in_user(clock_in: ClockIn):
    clockin_data = dict(clock_in)
    clockin_data["insert_date"] = datetime.now()
    result = clockin_collection.insert_one(clockin_data)
    return {"id": str(result.inserted_id)}

@app.get("/clock-in/{id}", response_model=dict)
async def get_clockin_record(id: str):
    record = clockin_collection.find_one({"_id": ObjectId(id)})
    if record:
        return clock_helper(record)
    raise HTTPException(status_code=404, detail="Record not found")

@app.get("/clock-in/filter/", response_model=List[dict])
async def filter_clockins(email: str = None, location: str = None, insert_datetime: str = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": datetime.strptime(insert_datetime, "%Y-%m-%d")}
    
    records = clockin_collection.find(query)
    return [clock_helper(record) for record in records]

@app.delete("/clock-in/delete/{id}", response_model=dict)
async def delete_clockin_record(id: str):
    result = clockin_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Clock-In record deleted"}
    raise HTTPException(status_code=404, detail="Record not found")

@app.put("/clock-in/update/{id}", response_model=dict)
async def update_clockin_record(id: str, clock_in: ClockInUpdate):
    clock = clock_in.dict(exclude_unset=True)
    updated_record = clockin_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": clock},
        return_document=ReturnDocument.AFTER
    )
    if updated_record:
        return {'message':'Updated element'}
    raise HTTPException(status_code=404, detail="Record not found")
