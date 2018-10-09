from flask_cors import CORS
from flask import render_template
from backend import db, app

cors = CORS(app, resources={"/api/*": {"origins": "*"}})

#front url
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

from .usr import *
from .dlg import *
