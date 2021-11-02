"""Server for Photocard Template Creator"""

from flask import (Flask, render_template, request, flash, session,
                redirect, Markup)
from model import connect_to_db

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    connect_to_db(app, "photocards")
    app.run(debug=True, host='0.0.0.0')