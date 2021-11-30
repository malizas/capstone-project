"""Server for Photocard Template Creator"""

from flask import (Flask, render_template, request, flash, session,
                redirect, Markup, jsonify)
from model import connect_to_db,db
import requests
import crud
import os

app = Flask(__name__)
app.secret_key = "dev"


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user', methods=['POST'])
def user_registration():
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.find_email(email):
        flash('Use already exist, please try again or login')
        return redirect('/login')
    else:
        crud.create_user(email, password)
        flash('Registration complete, please login')
        return redirect('/login')

@app.route('/login', methods=['POST'])
def user_login():
    """Logs the user in"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.find_email(email)

    if user and password==user.password:
        # this will store the user's information
        session['user_id'] = user.user_id
        session["user_email"] = user.email
        flash('Log in sucessful!')
    else:
        return redirect('/login')

    return redirect('/template_files')

@app.route('/logout', methods=["POST"])
def user_logout():
    """Logs the user out"""

    if session["user_email"]:
        session.pop("user_id", None)
        session.pop("user_email", None)
        return redirect("/")
    else:
        return redirect("/")

# USER FILES -----------------------------

@app.route('/template_files')
def files():
    user_temps = crud.temp_by_user(session["user_id"])
    return render_template('files.html', user_temps=user_temps)

@app.route('/create_template', methods=["POST"])
def create_template():
    crud.create_template("arial", "black", "white", crud.find_user(session["user_id"]))

    return redirect('/template_files')

@app.route('/delete_file/<template_id>', methods=["POST"])
def delete_template(template_id):
    crud.delete_template(template_id)

    return redirect('/template_files')


# USER'S TEMPLATES -----------------------------

@app.route('/template_creator/<template_id>')
def user_template(template_id):
    pc_temps = crud.template_by_pc_pick(template_id)
    photocards = crud.all_photocards()
    session["template_id"] = template_id

    return render_template('template-creator.html', photocards=photocards, pc_temps=pc_temps)

@app.route('/save_template', methods=["POST"])
def save_template():
    template_and_pcs = crud.template_by_pc_pick(session["template_id"])
    pcs_in_template = []
    for pc in template_and_pcs:
        pcs_in_template.append(pc.photocard_id)

    ids_from_template = request.form.getlist("pc_key[]")
    results = list(map(int, ids_from_template))
    print("PCS IN TEMPLATE HERE", pcs_in_template)
    print("PCS RESULTS", results)

    for pc_id in results:
        if pc_id not in pcs_in_template: #if pc in list but NOT in the pc_picked table
            crud.create_pc_picked(session["template_id"], pc_id)
    
    for pc in pcs_in_template:
        if pc not in results: #if pc NOT in the list but IS in the pc_picked table
            crud.delete_pc_in_temp(session["template_id"], pc)

    return 'Your progress has been saved!'

# TEMPLATE CREATOR -----------------------------

@app.route('/template_creator')
def template_creator():
    photocards = crud.all_photocards()
    return render_template('template-creator.html', photocards=photocards)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')