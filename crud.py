"""Create, Read, Update, Delete (CRUD) Functions"""

from model import User, Template, Photocard, db, connect_to_db

def create_user(email, password):
    """Creates a new user"""
    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user
def all_users():
    """returns all users"""
    return User.query.all()

def find_user(user_id):
    """returns user_id and email from User class"""
    return User.query.get(user_id)

def find_email(email):
    """Find a user using their email"""
    return User.query.filter(User.email == email).first()


def create_photocard(pc_name, pc_group, pc_album, pc_img):
    """Create a new photocard"""
    photocard = Photocard(pc_name=pc_name, pc_group=pc_group, pc_album=pc_album, pc_img=pc_img)

    db.session.add(photocard)
    db.session.commit()

def all_photocards():
    """Return all photocards"""
    return Photocard.query.all()

def pc_by_id(photocard_id):
    """Return a photocard by id"""
    return Photocard.query.get(photocard_id)

def pc_by_name(pc_name):
    """Return photocards by name, possible to return multiple"""
    return Photocard.query.filter(Photocard.pc_name==pc_name).all()

def pc_by_group(pc_group):
    """Return photocards by group, possible to return multiple"""
    return Photocard.query.filter(Photocard.pc_group==pc_group).all()

def pc_by_album(pc_album):
    """Return photocards by album, possible to return multiple"""
    return Photocard.query.filter(Photocard.pc_album==pc_album).all()


def create_template(font_family, font_color, bg_color, user):
    """Creates a new template"""
    template = Template(font_family=font_family, font_color=font_color, bg_color=bg_color, user=user)

    db.session.add(template)
    db.session.commit()

def temp_by_user(user):
    """Returns templates associated with user"""
    return Template.query.filter(Template.user_id == user).all()

def find_template(template_id):
    """Returns a template object using template_id"""
    return Template.query.get(template_id)


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)