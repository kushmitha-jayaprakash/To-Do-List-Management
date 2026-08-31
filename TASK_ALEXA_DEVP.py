import os
from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "todo_secret_key"

# Storage for tasks
tasks = {}
next_id = 1

# HTML/CSS User Interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List Management</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 30px auto; padding: 20px; }
        h2 { color: #333; }
        .card { background: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #ddd; }
        input[type="text"], input[type="number"] { padding: 8px; width: 65%; margin-right: 5px; }
        button { padding: 8px 15px; background: #28a745; color: white; border: none; cursor: pointer; border-radius: 3px; }
        button.delete { background: #dc3545; }
        button.update { background: #007bff; }
        ul { list-style-type: none; padding: 0; }
        li { background: #fff; border: 1px solid #eee; padding: 10px; margin-bottom: 5px; display: flex; justify-content: space-between; }
        .alert { padding: 10px; background: #e2e2e2; border-left: 5px solid #333; margin-bottom: 15px; }
    </style>
</head>
<body>
    <h2>📋 To-Do List Management System</h2>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        {% for message in messages %}
          <div class="alert">{{ message }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <div class="card">
        <h3>1. Insert Task</h3>
        <form action="/add" method="POST">
            <input type="text" name="task_name" placeholder="Enter task description..." required>
            <button type="submit">Add Task</button>
        </form>
    </div>

    <div class="card">
        <h3>4. Display Tasks</h3>
        {% if not tasks %}
            <p><i>The task list is currently empty.</i></p>
        {% else %}
            <ul>
            {% for tid, desc in tasks.items() %}
                <li><span><strong>ID {{ tid }}:</strong> {{ desc }}</span></li>
            {% endfor %}
            </ul>
        {% endif %}
    </div>

    <div class="card">
        <h3>3. Update Task</h3>
        <form action="/update" method="POST">
            <input type="number" name="task_id" placeholder="Task ID" required min="1">
            <input type="text" name="new_desc" placeholder="New description..." required>
            <button type="submit" class="update">Update</button>
        </form>
    </div>

    <div class="card">
        <h3>2. Delete Task</h3>
        <form action="/delete" method="POST">
            <input type="number" name="task_id" placeholder="Task ID to delete" required min="1">
            <button type="submit" class="delete">Delete</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    global next_id
    desc = request.form.get("task_name", "").strip()
    if desc:
        tasks[next_id] = desc
        flash(f"Task added successfully with ID {next_id}!")
        next_id += 1
    else:
        flash("Task description cannot be empty.")
    return redirect(url_for("index"))

@app.route("/update", methods=["POST"])
def update_task():
    try:
        tid = int(request.form.get("task_id"))
        new_desc = request.form.get("new_desc", "").strip()
        if tid in tasks:
            if new_desc:
                tasks[tid] = new_desc
                flash(f"Task ID {tid} updated successfully.")
            else:
                flash("New description cannot be empty.")
        else:
            flash(f"Error: Task ID {tid} does not exist.")
    except ValueError:
        flash("Invalid Task ID format.")
    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete_task():
    try:
        tid = int(request.form.get("task_id"))
        if tid in tasks:
            del tasks[tid]
            flash(f"Task ID {tid} deleted successfully.")
        else:
            flash(f"Error: Task ID {tid} does not exist.")
    except ValueError:
        flash("Invalid Task ID format.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
