
from pydantic import BaseModel,Field
from datetime import datetime,date
from typing import Optional



class Item(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    

class ItemUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[str]

class ClockIn(BaseModel):
    email: str
    location: str

class ClockInUpdate(BaseModel):
    email: Optional[str]
    location: Optional[str]
