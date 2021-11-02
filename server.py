"""Server for Photocard Template Creator"""

from flask import (Flask, render_template, request, flash, session,
                redirect, Markup)
from model import connect_to_db

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def homepage():
    return render_template('homepage.html')