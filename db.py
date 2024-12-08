from datetime import datetime

from pymongo import MongoClient

def connect_to_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['project2']  # db name
    print("Connected successfully to mongo ")
    return db


def validate_task(mission):
    if not mission.get("description"): # helps not to crash the app
        raise ValueError("Task description is required.")
    if "status" not in mission:
        mission["status"] = "Pending"  # Default to 'Pending'

    mission["createdAt"] = datetime.now()
    mission["updatedAt"] = datetime.now()
    return mission
