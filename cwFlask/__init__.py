from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/bookdb'
##app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/bookdb'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres:\vkstdtjyedaxni:4b01de47462557ea5888eb1e33c4bcbb79a68228ce83e321e6dab6ad8eae440b@ec2-3-223-242-224.compute-1.amazonaws.com:5432\dcd731teesdviv'
app.config['SECRET_KEY'] = 'secret'
database = SQLAlchemy(app)
login_manager = LoginManager(app)
from cwFlask import routes

