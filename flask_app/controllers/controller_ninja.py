from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_ninja, model_dojo

@app.route('/ninja/new')
def ninja_new():
    context = {
        'all_dojos': model_dojo.Dojo.get_all()
    }
    return render_template('ninja_new.html', **context)

@app.route('/ninja/create', methods = ['POST'])
def ninja_create():
    model_ninja.Ninja.create(request.form)
    return redirect ('/')

@app.route('/ninja/<int:id>')
def ninja_show(id):
    context = {
        'ninja'  : model_ninja.Ninja.get_one({'id': id})
    }
    return render_template('ninja_show.html', **context)

@app.route('/ninja/<int:id>/edit')
def ninja_edit(id):
    context = {
        'ninja'  : model_ninja.Ninja.get_one({'id': id})
    }
    return render_template('ninja_edit.html', **context)

@app.route('/ninja/<int:id>/update', methods = ['POST'])
def ninja_update(id):
    data = {
        **request.form,
        'id': id
    }
    model_ninja.Ninja.update_one(data)
    return redirect('/')

@app.route('/ninja/<int:id>/delete')
def ninja_delete(id):
    model_ninja.Ninja.delete_one({'id':id})
    return redirect('/')

#/ninjanew ->display
#/ninja/create ->action
#/ninja/<int:id> ->display
#/ninja/<int:id>/edit ->display
#/ninja/<int:id>/update ->action
#/band/<int:id>/delete ->action