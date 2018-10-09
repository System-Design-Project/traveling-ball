from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Cxl123456.@localhost:3306/traveling_ball'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='Secrets!'   #随意设置

db = SQLAlchemy(app)

from .route import *
