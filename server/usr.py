from flask import jsonify, request
from flask_login import login_user,logout_user,login_required,current_user
from server import db, app, login_manager
from .Handler.hd_base import require
from .models import User

@app.route('/api/newAccount', methods=['POST'])
@require('account', 'nickname', 'password')
def addNewUsr():
    response = {
        'code': 2
    }

    p_account = request.json.get('account',None)
    p_username = request.json.get('nickname',None)
    p_password = request.json.get('password',None)
    p_mail = request.json.get('mail',None)

    usr = User.query.get(p_account)
    print(usr)
    if (usr == None):
        response['code'] = 0
        newUser = User(account=p_account, nickname=p_username, password=p_password, mail=p_mail)
        db.session.add(newUser)
        db.session.commit()
        return jsonify(response)
    else :
        response['code'] = 1
        return jsonify(response)
    return jsonify(response)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.route('/api/login', methods=['POST'])
@require('account', 'password')
def Login():
    response = {
        'code': 3,
        'nickname': "err",
        'goalCoin': -1
    }

    account = request.json.get('account')
    password = request.json.get('password')

    usrLog = User.query.get(account)
    if usrLog == None:
        response['code'] = 1
    elif password != usrLog.password:
        response['code'] = 2
    elif password == usrLog.password:
        if not current_user:
            login_user(usrLog, False)
        elif current_user.is_authenticated:
            logout_user()
        login_user(usrLog, False)
        if current_user.is_authenticated:
            response['code'] = 0
            response['nickname'] = usrLog.nickname
            response['goalCoin']= usrLog.goalCoin
        # print(user)

    return jsonify(response)

@app.route('/api/logout', methods=['POST'])
@require('account')
@login_required
def logout():
    response = {
        'code': 1
    }
    logout_user()

    if not current_user or current_user.is_authenticated == False:
        response['code'] = 0

    return jsonify(response)
