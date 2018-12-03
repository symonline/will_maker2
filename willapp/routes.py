from flask import render_template, flash, redirect, url_for
from willapp import app
from willapp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'David'}
    posts = [
        {'author':{'username':'David'},
         'body':'What a beautiful weekend'
            },
        {
         'author': {'username':'Oshoke'},
         'body': 'Mission accomplished over the weekend'
            }
    ]
    return render_template('index.html', title='', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, Remember_me={}'.format(\
              form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)