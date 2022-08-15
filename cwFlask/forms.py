from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, EqualTo , Email
class registrationform(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    username = StringField(label = 'username', validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=9, max=16) ])
    confirmpassword = PasswordField(label='confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Signup')

class loginform(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=9, max=16) ])
    submit = SubmitField(label='Login')

class bookform(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=1, max=60)])
    author = StringField(label='Author', validators=[DataRequired(),Length(min=4, max=16) ])
    description = StringField(label='Description', validators=[DataRequired(), Length(min=10, max=400)])
    submit = SubmitField(label='Submit')