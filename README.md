# FastAPI CRUD Application

This project is a FastAPI application that performs CRUD (Create, Read, Update, Delete) operations for two entities: **Items** and **User Clock-In Records**. The app connects to a MongoDB database and offers multiple APIs with filtering and aggregation capabilities.

## Features

- **CRUD Operations**: Create, Read, Update, Delete for Items and Clock-In Records.
- **Filter Options**: Filter by email, expiry date, insert date, quantity, location.
- **MongoDB Aggregation**: Group and count items by email.
- **Swagger Documentation**: Auto-generated API documentation using FastAPI's Swagger UI.

## Prerequisites

- **Python 3.8+**
- **MongoDB** (Use MongoDB Atlas or a local instance)
- **Git** (for version control)

## Installation and Setup


1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-crud-app.git

cd fastapi-crud-app

2. Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Configure MongoDB connection
Modify database.py to set up your MongoDB connection. 
You can use a MongoDB URI string for Atlas or local MongoDB instance.


5. Run the application

uvicorn app.main:app --reload
The app should now be running on http://127.0.0.1:8000.


6. Access the Swagger Documentation
Go to http://127.0.0.1:8000/docs to view the Swagger UI and test the APIs.

