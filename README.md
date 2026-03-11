# Task Manager MVC Application

## Project Overview
Task Manager MVC Application built using **Python Flask and MySQL**.  
This application allows users to **create, view, update, delete and search tasks**.

---

## Technologies Used
- Python
- Flask
- MySQL
- HTML
- CSS
- GitHub

---

## Features
- Create Task
- Read Tasks
- Update Task
- Delete Task
- Search Task

---

## Database Structure

Table: **tasks**

| Field | Type | Description |
|------|------|-------------|
| id | INT | Primary Key |
| title | VARCHAR(100) | Task title |
| description | TEXT | Task description |
| duedate | DATE | Task due date |
| status | VARCHAR(20) | Task status |
| remarks | VARCHAR(200) | Additional notes |
| created_on | TIMESTAMP | Created time |
| updated_on | TIMESTAMP | Last updated time |

---

## Project Structure

task-manager-mvc
│
├── app.py
│
├── templates
│ ├── index.html
│ ├── add_task.html
│ └── edit_task.html
│
├── static
│ └── style.css
│
└── README.md


---

## Run Instructions

Install dependencies:

pip install flask
pip install flask-mysqldb


Run the application:

python app.py

Open in browser:

http://127.0.0.1:5000

---

## MVC Architecture

**Model:** MySQL Database (tasks table)  
**View:** HTML Templates (index.html, add_task.html, edit_task.html)  
**Controller:** Flask application (app.py)
