from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png"


"""Models for Blogly."""
class User(db.Model):
    """Site User"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String, default=DEFAULT_IMG_URL)



class Post(db.Model):
    """User Posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User')

    @property
    def format_date(self):
        """Return better formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")