# Mission Management Application (To-Do App)

This is a simple command-line **Mission Management Application** built using **Python** and **MongoDB**.
The application allows users to add, view, delete, and update missions' statuses through a menu-driven interface.

---

## 📌 **Features**

- Add a new mission with a description.
- View all missions in the database.
- Update the status of any existing mission.
- Delete a mission by its ID.
- Exit the application when done.

---

## 🛠️ **Technologies Used**

- **Python** for backend logic.
- **MongoDB** for database operations.
- **pymongo** library for connecting and interacting with MongoDB.

---

## 🖥️ **Setup**

1. **Set up MongoDB**:
   - Ensure you have MongoDB installed locally or use a cloud-based MongoDB instance.
   - Start MongoDB locally on `localhost:27017` or update the connection string in `db.py`.

2. **Install dependencies**:
   - Clone the repository and run:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application**:
   - Start the application with:
     ```bash
     python index.py
     ```

---

## 🚀 **Usage**

Once the application runs, you'll be greeted with a menu:


Select options by entering their corresponding numbers.

---

## 📊 **Database Schema**

The MongoDB collection `missions` contains documents with the following fields:

| Field          | Type         | Description                 |
|----------------|--------------|-----------------------------|
| `_id`         | ObjectId     | Automatically generated ID |
| `description`  | String       | Description of the mission |
| `status`       | String       | Mission's current status |
| `createdAt`    | DateTime     | Timestamp of creation |
| `updatedAt`    | DateTime     | Timestamp of last status update |

---


