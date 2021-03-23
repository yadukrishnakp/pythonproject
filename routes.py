from flask import Flask, render_template, redirect, flash
from models import User
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yadu'}
    posts = [
        {
            'author': {'username': 'yadu'},
            'body': 'wondering'
        },
        {
            'author': {'username': 'krishna'},
            'body': 'amazing'
        }]
    return render_template('index.html', user=user, title='home', posts=posts)


@app.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('index')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
