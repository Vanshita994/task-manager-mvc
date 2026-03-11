**Project Overview**
Task Manager MVC Application built using Python Flask and MySQL.
This application allows users to create, view, update, delete and search tasks.

**Technologies Used**
Python
Flask
MySQL
HTML
CSS
GitHub

**Features**
Create Task
Read Tasks
Update Task
Delete Task
Search Task

**Database Structure**
Table: tasks

id INT PRIMARY KEY
title VARCHAR(100)
description TEXT
duedate DATE
status VARCHAR(20)
remarks VARCHAR(200)
created_on TIMESTAMP
updated_on TIMESTAMP

**Project Structure**
task-manager-mvc
│
├── app.py
├── templates
├── static
└── README.md

**Run Instructions**
pip install flask
pip install flask-mysqldb
python app.py

Open:
http://127.0.0.1:5000
