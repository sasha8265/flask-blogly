"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def list_users():
    """List all existing users"""

    users = User.query.all()
    return render_template("list.html", users=users)


@app.route('/<user_id>')
def show_user_detals(user_id):
    user = User.query.get(user_id)
    return render_template('details.html', user=user)


@app.route('/add-user')
def show_add_user_form():
    return render_template("form.html")


@app.route('/', methods=["POST"])
def add_user():
    first_name = request.form["first_name"] 
    last_name = request.form["last_name"] 
    image_url = request.form["image_url"]
    image_url = image_url if image_url else None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()