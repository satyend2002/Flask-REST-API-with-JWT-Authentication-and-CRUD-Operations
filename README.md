# Flask REST API with JWT Authentication and CRUD Operations

This project is a RESTful API built using **Python and Flask** to manage book records.  
It allows users to perform **CRUD operations** (Create, Read, Update, Delete) on a SQL database.

## Features

- User Registration API
- User Login with JWT Authentication
- Secure password hashing
- Protected endpoints using JWT tokens
- CRUD operations for items
- Request validation using Flask-RESTful reqparse
- SQL database integration
- Clean project structure (Models, Controllers, Resources)



## Technologies Used
- Python
- Flask
- SQL / SQLite
- REST API



## API Endpoints

### Authentication

| Method | Endpoint | Description |
|------|------|------|
| POST | /register | Register new user |
| POST | /login | Login user and generate JWT token |


### Items

| Method | Endpoint | Description |
|------|------|------|
| POST | /items | Create new item (JWT required) |
| GET | /items | Get all items |
| GET | /items/<id> | Get item by id |
| PUT | /items/<id> | Update item (JWT required) |
| DELETE | /items/<id> | Delete item (JWT required) |




## How to Run the Project

### 1. Clone the repository
git clone https://github.com/YOURUSERNAME/flask-book-management-api.git

### 2. Navigate to the project folder
cd flask-book-management-api

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
python app.py


## Author
Satyendra Dwivedi
Backend Developer | Python | Flask
