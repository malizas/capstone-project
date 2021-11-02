"""Create, Read, Update, Delete (CRUD) Functions"""

from model import User, File, Template, Photocard, db, connect_to_db

def create_user(email, password):
    """Creates a new user"""
    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def find_email(email):
    """Find a user using their email"""
    return User.query.filter(User.email == email).first()


def create_file(title):
    """Creates a file"""
    template_title = File(title=title)

    db.session.add(template_title)
    db.sesion.commit()

    return template_title

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app, "photocards")