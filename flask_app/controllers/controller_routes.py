from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_dojo, model_ninja #import all model tables 


@app.route('/')
def index():
    context = {
        'all_dojos': model_dojo.Dojo.get_all() 
    }
    print(context)
    return render_template('index.html', **context)

#@app.errorhandler(404)
#def server_error(e):
#    print('running error function')
#    return render_template('error.html')