from cwFlask import database,login_manager
from flask_login import UserMixin
from flask import redirect, url_for

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))

class User(database.Model,UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(15), unique=True, nullable=False)
    email =  database.Column(database.String(120), unique=True, nullable=False)
    password =  database.Column(database.String(16), nullable=False)
    books = database.relationship('Book', backref='bookrel')

    def __repr__(self):
        return f'{self.username} : {self.email}'

class Book(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(60), unique=True, nullable=False)
    author = database.Column(database.String(120), unique=False, nullable=False)
    description = database.Column(database.String(400), unique=False, nullable=False)
    book_fk = database.Column(database.Integer, database.ForeignKey('user.id'))