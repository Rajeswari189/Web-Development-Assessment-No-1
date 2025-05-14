from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # required for flash messaging

# Load project data
def load_projects():
    with open('.devcontainer/projects.json') as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    projects_data = load_projects()
    return render_template("projects.html", projects=projects_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if not name or not message:
            flash("Please fill out all fields.")
            return redirect(url_for("contact"))
        flash(f"Thanks for reaching out, {name}!")
        return redirect(url_for("home"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
