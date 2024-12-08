from datetime import datetime

from bson import ObjectId

from db import validate_task



# add a new mission (1)
def add_mission(db, description):
    mission = {
        "description": description,
    }
    try:
        validated = validate_task(mission)
        db.missions.insert_one(validated)
        print("Mission added successfully!")
    except ValueError as error:
        print("Validation Error:", error)

# all the missions (2)
def get_missions(db):
    missions = list(db.missions.find())  # Query all missions
    if not missions:
        print("You have no missions")
    else:
        print("Missions:")
        for item in missions:
            print(
                f"ID: {item['_id']} | Description: {item['description']} | "
                f"Status: {item['status']} | Created At: {item['createdAt']} | Updated At: {item['updatedAt']}"
            )


# update mission status (3)
def update_status(db, mission_id, new_status):
    try:
        result = db.missions.update_one(
            {"_id": ObjectId(mission_id)},
            {"$set": {"status": new_status, "updatedAt": datetime.now()}}
        )
        if result.modified_count > 0:
            print("status has been updated")
        else:
            print("Id is incorrect")
    except Exception as error:
        print("error when updating: internal error")

# delete a mission (4)
def delete_mission(db, mission_id):
    try:
        result = db.missions.delete_one({"_id": ObjectId(mission_id)})
        if result.deleted_count > 0:
            print("Mission deleted successfully!")
        else:
            print("No mission found with the provided ID.")
    except Exception as error:
        print("Error deleting mission: internal error ")