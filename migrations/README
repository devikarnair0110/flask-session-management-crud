Single-database configuration for Flask.
# Student Management System

A simple  Student Management System developed using Flask
This project demonstrates Session Management along with CRUD operations for managing student records.

## Advanced Flask Technology

**Session Management**

Flask sessions are used to maintain the user's login status and protect important pages such as the Dashboard and Student List.



## Features

* User Login using Flask Session
* Dashboard
* Add Student
* View Student List
* Edit Student
* Delete Student
* Logout
* Form validation using Flask-WTF
* Database integration using Flask-SQLAlchemy
* Database migration using Flask-Migrate
* HTML templates using Jinja2
* CSS styling



## Technologies Used

* Python
* Flask
* Flask-WTF
* Flask-SQLAlchemy
* Flask-Migrate
* Jinja2
* HTML
* CSS
* SQLite



## Project Structure


student_management/
│
├── app.py
├── models.py
├── forms.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   └── edit_student.html
│
├── static/
│   └── style.css
│
└── migrations/

## Application Workflow


Home
  ↓
Login
  ↓
Session Created
  ↓
Dashboard
  ↓
Student List
  ↓
Add / Edit / Delete Student
  ↓
Logout
  ↓
Session Cleared


## Installation

### 1. Create a Virtual Environment


python -m venv venv

### 2. Activate Virtual Environment

**Windows PowerShell:**

venv\Scripts\Activate.ps1


If PowerShell gives an execution policy error, use Command Prompt:

venv\Scripts\activate
``

### 3. Install Required Packages

pip install -r requirements.txt



## Database Setup

Initialize Flask-Migrate:


flask --app app db init

Create the migration:


flask --app app db migrate -m "Create student table"


Apply the migration:


flask --app app db upgrade

> `flask db init` is required only the first time when the `migrations` folder does not already exist.



## Run the Application

Run:


python app.py

The application will start on:


http://127.0.0.1:5000


Open the address in a web browser.



## Login

Enter any username and password that are not empty.

Example:


Username: admin
Password: admin123

After successful login, the username is stored in the Flask session.


## Session Management

The project uses Flask's `session` object.

### Create Session


session["username"] = form.username.data

### Check Session


if "username" not in session:
    return redirect(url_for("login"))

### Logout

session.pop("username", None)


The session is cleared when the user logs out.



## CRUD Operations

### Create

Add a new student to the database.

### Read

Display all students in the Student List.

### Update

Edit existing student information.

### Delete

Remove a student from the database.



## Database Model

The Student table contains:

| Field  | Type    |
| ------ | ------- |
| id     | Integer |
| name   | String  |
| email  | String  |
| course | String  |



## Main Routes

| Route                  | Function       |
| ---------------------- | -------------- |
| `/`                    | Home           |
| `/login`               | User Login     |
| `/dashboard`           | Dashboard      |
| `/students`            | View Students  |
| `/student/add`         | Add Student    |
| `/student/edit/<id>`   | Edit Student   |
| `/student/delete/<id>` | Delete Student |
| `/logout`              | Logout         |



## Requirements

The required Python packages are listed in `requirements.txt`.

Flask
Flask-WTF
Flask-SQLAlchemy
Flask-Migrate
email-validator


Install them using:


pip install -r requirements.txt




## Learning Outcomes

Through this project, the following concepts are demonstrated:

* Flask Routing
* Flask Session Management
* HTML Templates
* Jinja2 Template Engine
* Flask-WTF Forms
* Form Validation
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite Database
* CRUD Operations
* Static CSS Files

