"""Models for Photocard Template Creator"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    """User Information"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    #files = list of File objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class File(db.Model):
    """File Information"""

    __tablename__ = "files"

    file_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship("User", backref="files")
    #templates = list of Template objects


    def __repr__(self):
        return f'<File file_id={self.file_id} title={self.title}>'


class Template(db.Model):
    """Template Creator Information"""

    __tablename__ = "template_creator"

    template_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    photocard_id = db.Column(db.Integer, db.ForeignKey('photocards.photocard_id'))
    file_id = db.Column(db.Integer, db.ForeignKey('files.file_id'))

    photocards = db.relationship("Photocard", backref="templates")
    file = db.relationship("File", backref="templates")

    def __repr__(self):
        return f'<Template template_id={self.template_id}>'


class Photocard(db.Model):
    """Photocard Information"""

    __tablename__ = "photocards"

    photocard_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    pc_name = db.Column(db.String)
    pc_group = db.Column(db.String)
    pc_album = db.Column(db.String)
    pc_img = db.Column(db.String)

    #templates = list of Template objects

    def __repr__ (self):
        return f'<Photocard photocard_id={self.photocard_id} pc_name={self.pc_name} pc_group={self.pc_group} pc_album={self.pc_group}>'


def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Conntect to db!")

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app, "photocards")