from server import db
from flask_login import AnonymousUserMixin

class Users(db.Model):
    #__bind_key__ = 'xnet_master'
    __tablename__ = 'users'

    account = db.Column(db.String(12), primary_key=True)
    nickname = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    goalCoin = db.Column(db.Integer, nullable=False)

    def __init__(self, nickname, mail, password):
        self.nickname = nickname
        self.mail = mail
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.account
