from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html", all_dojos=Dojo.get_all())


@app.route('/create_ninja/',methods=['POST'])
def create():
    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    Ninja.save(data)
    return redirect('/dojos') 

@app.route('/dojos')
def dojos():
    return render_template("display_dojo.html", all_dojos=Dojo.get_all())


@app.route('/create_dojo/', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')


@app.route('/ninjas')
def ninjas():
    return render_template("display_ninja.html",all_ninjas=Ninja.get_all())


@app.route('/show/<int:dojo_id>')
def diplay_ninjas(dojo_id):
    data =  {
        "id":dojo_id
    }
    return render_template("display_ninja.html", all_dojos_w_ninjas=Dojo.get_dojo_with_ninjas(data))


@app.route('/edit_page/<int:ninja_id>')
def edit_page(ninja_id):
    data = {
        'id': ninja_id
    }
    ninja = Ninja.get_one(data)
    return render_template("edit_page.html", ninja = ninja)


@app.route('/update/<int:ninja_id>', methods=['POST'])
def update(ninja_id):
    data = {
        'id': ninja_id,
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }
    Ninja.update(data) #after we update the info we then need to get the new data so we 
    # so we create a new dictionary to get that data and redirect to the corresponding page
    data2 = {
        'id': ninja_id
    }
    ninja = Ninja.get_one(data2)
    return redirect(f"/show/{ninja.dojo_id}") # when we parse info in a redirect be careful with syntax

@app.route('/delete/<int:ninja_id>')
def delete(ninja_id):
    data = {
        'id': ninja_id,
    }
    Ninja.destroy(data)
    return redirect('/')