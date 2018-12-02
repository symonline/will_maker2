from flask import render_template,url_for
from willapp import app
from willapp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'username':'David'}
    posts=[
        {'author':{'username':'David'},
         'body':'What a beautiful weekend'
            },
        {
         'author': {'username':'Oshoke'},
         'body': 'Mission accomplished over the weekend'
            }
    ]
    return render_template('index.html',title='',user=user,posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In',form=form)