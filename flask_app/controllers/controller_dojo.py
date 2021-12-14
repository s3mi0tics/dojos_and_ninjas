from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_dojo, model_ninja

@app.route('/dojo/new')
def dojo_new():
    return render_template('dojo_new.html')

@app.route('/dojo/create', methods = ['POST'])
def dojo_create():
    model_dojo.Dojo.create(request.form)
    return redirect ('/')

@app.route('/dojo/<int:id>')
def dojo_show(id):
    context = {
        'dojo'  : model_dojo.Dojo.get_one({'id': id}),
        'all_ninjas' :model_ninja.Ninja.get_all_of_dojo({'id':id})
    }
    return render_template('dojo_show.html', **context)

@app.route('/dojo/<int:id>/edit')
def dojo_edit(id):
    context = {
        'dojo'  : model_dojo.Dojo.get_one({'id': id})
    }
    return render_template('dojo_edit.html', **context)

@app.route('/dojo/<int:id>/update', methods = ['POST'])
def dojo_update(id):
    data = {
        **request.form,
        'id': id
    }
    model_dojo.Dojo.update_one(data)
    return redirect('/')

@app.route('/dojo/<int:id>/delete')
def dojo_delete(id):
    model_dojo.Dojo.delete_one({'id':id})
    return redirect('/')

#/dojonew ->display
#/dojo/create ->action
#/dojo/<int:id> ->display
#/dojo/<int:id>/edit ->display
#/dojo/<int:id>/update ->action
#/band/<int:id>/delete ->action