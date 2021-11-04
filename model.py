"""Models for Photocard Template Creator"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

association_table = db.Table('pc_picked',
                    db.Column('template_id', db.Integer, db.ForeignKey('templates.template_id')),
                    db.Column('photocard_id', db.Integer, db.ForeignKey('photocards.photocard_id'))
                    )

class User(db.Model):
    """User Information"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    #templates = list of Template objects associated with a certain user

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Template(db.Model):
    """Template Creator Information"""

    __tablename__ = "templates"

    template_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    font_family = db.Column(db.String)
    font_color = db.Column(db.String)
    bg_color = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    users = db.relationship("User", backref="templates")
    #photocards = db.relationship("Photocard", secondary="pc_picked", backref="templates")
    photocards = db.relationship("Photocard", secondary=association_table)

    def __repr__(self):
        return f'<Template template_id={self.template_id} user_id={self.user_id}>'


# class PC_Picked(db.Model):
#     """Photocards Picked for the Template"""

#     __tablename__= "pc_picked"

#     pc_picked_id = db.Column(db.Integer,
#                     autoincrement=True,
#                     primary_key=True)
#     template_id = db.Column(db.Integer, db.ForeignKey('templates.template_id'), nullable=False)
#     photocard_id = db.Column(db.Integer, db.ForeignKey('photocards.photocard_id'), nullable=False)

#     def __repr__(self):
#         return f'<PC_Picked pc_picked_id={self.pc_picked_id} template_id={self.template_id} photocard_id={self.photocard_id}>'

class Photocard(db.Model):
    """Photocard Information"""

    __tablename__ = "photocards"

    photocard_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    pc_name = db.Column(db.String(30))
    pc_group = db.Column(db.String(30))
    pc_album = db.Column(db.String(50))
    pc_img = db.Column(db.String)


    def __repr__ (self):
        return f'<Photocard photocard_id={self.photocard_id} pc_name={self.pc_name} pc_album={self.pc_album} pc_group={self.pc_group}>'


def connect_to_db(app):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///photocards"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Conntect to db!")

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)