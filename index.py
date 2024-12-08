from db import connect_to_db
from todo import add_mission, get_missions, update_status, delete_mission


def main():
    db = connect_to_db()

    while True:
        print("\nMission Management Menu:")
        print("1 - Add a new mission")
        print("2 - View all missions")
        print("3 - Update a mission's status")
        print("4 - Delete a mission")
        print("5 - Exit")

        choice = input("Select an option:\n ")

        if choice == "1":
            description = input("Enter details \n ")
            add_mission(db, description)
        elif choice == "2":
            get_missions(db)
        elif choice == "3":
            mission_id = input("Enter Id \n ")
            new_status = input("Enter Status \n ")
            update_status(db, mission_id, new_status)
        elif choice == "4":
            mission_id = input("Enter Id to delete a mission \n ")
            delete_mission(db, mission_id)
        elif choice == "5":
            print("Existin...")
            break
        else:
            print("Choose a number between 1-5")


if __name__ == "__main__":
    main()
