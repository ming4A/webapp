from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required
from flask_wtf import Form
class LoginForm(Form):
    username = StringField("Username:",validators=[Required()])
    password = PasswordField('Password:',validators=[Required()])
    submit = SubmitField('Submit')
class RigisterForm(Form):
    username = StringField("Username:",validators=[Required()])
    password = PasswordField('Password:',validators=[Required()])