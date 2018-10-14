from flask_cors import CORS
from flask import render_template
from server import db, app

cors = CORS(app, resources={"/api/*": {"origins": "*"}})

#front url
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

from .usr import *
from .skin_and_prop import *
from .game import *
