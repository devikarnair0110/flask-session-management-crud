from flask import Flask, render_template, redirect, url_for, session, flash
from flask_migrate import Migrate

from models import db, Student
from forms import LoginForm, StudentForm


app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = "student-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize Database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        session["username"] = form.username.data

        flash("Login successful!", "success")

        return redirect(url_for("dashboard"))

    return render_template("login.html", form=form)


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


@app.route("/students")
def students():

    if "username" not in session:
        return redirect(url_for("login"))

    students = Student.query.all()

    return render_template(
        "students.html",
        students=students
    )


@app.route("/student/add", methods=["GET", "POST"])
def add_student():

    if "username" not in session:
        return redirect(url_for("login"))

    form = StudentForm()

    if form.validate_on_submit():

        student = Student(
            name=form.name.data,
            email=form.email.data,
            course=form.course.data
        )

        db.session.add(student)
        db.session.commit()

        flash("Student added successfully!", "success")

        return redirect(url_for("students"))

    return render_template(
        "add_student.html",
        form=form
    )


@app.route("/student/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    if "username" not in session:
        return redirect(url_for("login"))

    student = db.get_or_404(Student, id)

    form = StudentForm(obj=student)

    if form.validate_on_submit():

        student.name = form.name.data
        student.email = form.email.data
        student.course = form.course.data

        db.session.commit()

        flash("Student updated successfully!", "success")

        return redirect(url_for("students"))

    return render_template(
        "edit_student.html",
        form=form
    )


@app.route("/student/delete/<int:id>")
def delete_student(id):

    if "username" not in session:
        return redirect(url_for("login"))

    student = db.get_or_404(Student, id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully!", "success")

    return redirect(url_for("students"))


@app.route("/logout")
def logout():

    session.pop("username", None)

    flash("Logged out successfully!", "success")

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)