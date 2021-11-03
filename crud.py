"""Create, Read, Update, Delete (CRUD) Functions"""

from model import User, File, db, connect_to_db

def create_user(email, password):
    """Creates a new user"""
    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def find_email(email):
    """Find a user using their email"""
    return User.query.filter(User.email == email).first()

def create_template(font_family, font_color, bg_color):
    """Creates a new template"""
    template = User(font_family=font_family, font_color=font_color, bg_color=bg)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app, "photocards")