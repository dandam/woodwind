from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'andre3000'}
    posts = [
        {
            'author': {'username': 'Domino'},
            'body': 'First name is Fats!'
        },
        {
            'author': {'username': 'Wanda'},
            'body': 'Drugstore rock and roll!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)