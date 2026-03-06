from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/courses")
def course():
    return render_template("course.html")
@app.route("/admin")
def admin():
    users = [
        {"id": 1, "name": "Md", "role": "Admin"},
        {"id": 2, "name": "Ali", "role": "Teacher"},
        {"id": 3, "name": "Sara", "role": "Student"},
    ]
    courses = [
        {"id": "C101", "name": "Python Programming"},
        {"id": "C102", "name": "Web Development"},
        {"id": "C103", "name": "Database Management"},
    ]
    reports = [
        {"title": "Student Performance Report"},
        {"title": "Course Enrollment Report"},
        {"title": "System Usage Report"},
    ]
    return render_template("admin.html",users=users,courses=courses,reports=reports)