from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'World' } # fake user
    return render_template("index.html",
        title = 'Welcome',
        user = user)