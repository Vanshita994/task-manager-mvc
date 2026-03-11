from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)

# Database Connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="root",   # agar mysql password hai to yaha likho
    database="taskdb"
)

# Home Page - Show Tasks
@app.route('/')
def index():
    cur = db.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return render_template("index.html", tasks=tasks)

# Add Task
@app.route('/search', methods=['POST'])
def search():
    search = request.form['search']

    cur = db.cursor()
    cur.execute("SELECT * FROM tasks WHERE title LIKE %s", ('%' + search + '%',))
    tasks = cur.fetchall()

    return render_template("index.html", tasks=tasks)
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    duedate = request.form['duedate']
    status = request.form['status']

    cur = db.cursor()
    cur.execute(
        "INSERT INTO tasks(title,description,duedate,status) VALUES(%s,%s,%s,%s)",
        (title, description, duedate, status)
    )
    db.commit()

    return redirect('/')

# Delete Task
@app.route('/delete/<id>')
def delete(id):
    cur = db.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()

    return redirect('/')

@app.route('/edit/<id>')
def edit(id):
    cur = db.cursor()
    cur.execute("SELECT * FROM tasks WHERE id=%s",(id,))
    task = cur.fetchone()
    return render_template("edit_task.html", task=task)

@app.route('/update/<id>', methods=['POST'])
def update(id):
    title = request.form['title']
    description = request.form['description']
    duedate = request.form['duedate']
    status = request.form['status']

    cur = db.cursor()
    cur.execute(
        "UPDATE tasks SET title=%s, description=%s, duedate=%s, status=%s WHERE id=%s",
        (title, description, duedate, status, id)
    )
    db.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)