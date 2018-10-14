from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Cxl123456.@localhost:3306/traveling_ball'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='Secrets!'   #随意设置
app.config['JSON_AS_ASCII']=False

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)
#认证加密程度
login_manager.session_protection='strong'

from .route import *
