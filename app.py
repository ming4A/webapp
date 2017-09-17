#coding:utf-8
from flask import Flask,render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from dataclass import User
from werkzeug.security import generate_password_hash as generate_password_hash
app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'key'
toolbar = DebugToolbarExtension(app)
@app.route('/')
def index():
    return render_template('base.html',name = u"陌生人")
@app.route('/user/<id>')
def userindex(id):
    return render_template('base.html',name = id)
@app.route('/home')
def homeindex():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(host = 'localhost',port = 4000,debug= app.debug)
