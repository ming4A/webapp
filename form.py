from wtforms import StringField,SubmitField,PasswordField,SelectField
from wtforms import ValidationError
from wtforms.validators import Required,EqualTo,Email
from flask_wtf import Form
from Model import User,Area
class LoginForm(Form):
    username = StringField("Username:",validators=[Required()])
    password = PasswordField('Password:',validators=[Required()])
    submit = SubmitField('Submit')
class RegisterForm(Form):
    email = StringField("Email:",validators=[Required(),Email()])
    username = StringField("Username:",validators=[Required()])
    password = PasswordField('Password:',validators=[Required(),EqualTo('confirm_pw',message="Password doesn't match!")])
    confirm_pw = PasswordField('Confirm your password:',validators=[Required()])
    choices = SelectField("Choose the area:",choices=[('1','2')])
    submit = SubmitField("Register")
    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("This email-address has been registered")
    def validate_username(self,field):
        if User.query.filter_by(name = field.data).first():
            raise ValidationError("This username has been registered")