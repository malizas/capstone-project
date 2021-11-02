"""Create, Read, Update, Delete (CRUD) Functions"""

from model import User, File, Template, Photocard, db, connect_to_db

def create_user(email, password):
    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_file(title):
    template_title = File(title=title)

    db.session.add(template_title)
    db.sesion.commit()

    return template_title

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app, "photocards")