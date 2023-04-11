""" Models for digital planner """

from flask_sqlalchemy import SQLAlchemy
from json import dumps


db = SQLAlchemy()


class User(db.Model):
    """ A user. """

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def to_json(self):
        """ Returns data of object. """

        return {'first_name': f"{self.fname}",
                'last_name': f"{self.lname}",
                'username': f"{self.username}",
                'email': f"{self.email}",
                'password': f"{self.password}",
                'interests': f"{self.interests.game.name}"}

    def __repr__(self):
        return f"<Id = {self.id}, Name = {self.fname} {self.lname}>"


class Events(db.Model):
    """ A monthly event. """

    __tablename__ = 'events'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Id = {self.id} Name = {self.name}>"


class WeeklyTasks(db.Model):
    """ A weekly task. """

    __tablename__ = 'weeklytasks'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Id = {self.id} Name = {self.name}>"


class ToDoTasks(db.Model):
    """ A todo task. """

    __tablename__ = 'todotasks'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Id = {self.id} Name = {self.name}>"


class UserEvents(db.Model):
    """ Events created by a user. """

    __tablename__ = 'userevents'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)

    def __repr__(self):
        return f"<Id = {self.id} User ID = {self.user_id} Event ID = {self.event_id}>"


class UserWeeklyTasks(db.Model):
    """ Weekly tasks created by users. """

    __tablename__ = 'userweeklytasks'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    weekly_id = db.Column(db.Integer, db.ForeignKey(
        'weeklytasks.id'), nullable=False)

    def __repr__(self):
        return f"<Id = {self.id} User ID = {self.user_id} Weekly ID = {self.weekly_id}>"


class UserToDoTasks(db.Model):
    """ To do tasks created by a user. """

    __tablename__ = 'todotasks'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey(
        'todotasks.id'), nullable=False)

    def __repr__(self):
        return f"<Id = {self.id} User ID = {self.user_id} To Do ID = {self.todo_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///digital_planner", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
