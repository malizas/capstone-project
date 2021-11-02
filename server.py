"""Server for Photocard Template Creator"""

from flask import (Flask, render_template, request, flash, session,
                redirect, Markup)
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user', method=["POST"])
def user_registration():
    email = request.form.get("email")
    password = request.form.get("password")

    if crud.find_email(email):
        flash('Use already exist, please try again or login')
    else:
        crud.create_user(email, password)
        flash('Registration complete, please login')

    return redirect('/')


# @app.route('/login', method=["POST"])
# def user_login():
#     email = request.form.get("email")
#     password = request.form.get("password")

#     user = crud.find_email(email)

#     if user and password == user.email:
#         session['user_id'] = user.user_id
#         flash('Sucessfully logged in!')
#     else:
#         flash('Login failed, please double check email or password')

#     return redirect('/')


if __name__ == '__main__':
    connect_to_db(app, "photocards")
    app.run(debug=True, host='0.0.0.0')