#coding:utf-8
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask import flash, redirect, url_for
from form import LoginForm, RegisterForm
from ext import db
from dataclass import User, Area
from consts import DB_URI
from flask_login import login_required
from werkzeug.security import generate_password_hash as get_hash
from werkzeug.security import check_password_hash as check_hash
app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
toolbar = DebugToolbarExtension(app)
db.init_app(app)
area_box = []
@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()
    users = [
       User("woshimg009", "woshikj009", "hellohanming@163.com"),
        User("mg009", "woshikj009", "hellohanming@164.com"),
        User("woshimg008", "woshikj009", "hellohanming@165.com"),
     ]
    areas = [
        Area("东区"), 
        Area("西区"), 
        Area("南区"),
    ]
    db.session.add_all(areas)
    db.session.add_all(users)
    db.session.commit()
    global area_box
    area_box = map(lambda e:(str(e.area_index), e.area_name),Area.query.all())
@app.route('/')
def index():
    return render_template('base.html',name = u"陌生人")
@app.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    username = request.args.get('username')
    if username and not form.username.data:
        form.username.data = username
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(name=username).first()
        if user is None:
            flash("The user is not exist.")
        elif  not check_hash(user.pw,form.password.data):
            flash("Wrong Password!")
            form.password.data = ''
        else:
            return redirect(url_for('userindex',id = username))
    return render_template('base.html',name = None,form = form,register = True)
@app.route('/user/<id>')
def userindex(id):
    return render_template('base.html',name = id,form = None)
@app.route('/home') 
def homeindex():
    return render_template('home.html')
@app.route('/register',methods = ['POST','GET'])
def register():
    form = RegisterForm()
    form.choices.choices = area_box
    if form.validate_on_submit():
        '''change password 2 password_hash'''
        form.password.data = get_hash(form.password.data)
        user = User(
            name = form.username.data,
            pw = form.password.data,email = form.email.data,
            area_index = int(form.choices.data)
            )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login',username = form.username.data))
    return render_template('register.html',form = form)
if __name__ == '__main__':
    app.run(host = 'localhost',port = 4000,debug= app.debug)