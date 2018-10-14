from flask import jsonify, request
from flask_login import login_required
from server import db, app
from .Handler.hd_base import require
from .models import User, Prop, Skin, User_Props, User_Skins

@app.route('/api/skins/user/<account>')
@login_required
def getUserSkins(account):
    response = {
        'code': 1,
        'skinlist': None
    }
    skinidlist = User_Skins.query.filter_by(account=account).all()

    if not skinidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        skinlist = []
        for i in skinidlist:
            tmpSkin = {
                'skinID': i.skinID,
                'skinsName': i.skinMsg.skinName,
                'description': i.skinMsg.description,
                'skinsValue': i.skinMsg.value,
                'isInStore': i.skinMsg.isInStore
            }
            skinlist.append(tmpSkin)
        response['skinlist'] = skinlist

    return jsonify(response)

@app.route('/api/skins/all')
@login_required
def getSkinsAll():
    response = {
        'code': 1,
        'skinlist': None
    }
    skinidlist = Skin.query.all()

    if not skinidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        skinlist = []
        for i in skinidlist:
            tmpSkin = {
                'skinID': i.skinID,
                'skinsName': i.skinName,
                'description': i.description,
                'skinsValue': i.value,
                'isInStore': i.isInStore
            }
            skinlist.append(tmpSkin)
        response['skinlist'] = skinlist

    return jsonify(response)

@app.route('/api/skins/store')
@login_required
def getSkinsInstore():
    response = {
        'code': 1,
        'skinlist': None
    }
    skinidlist = Skin.query.filter_by(isInStore=True).all()

    if not skinidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        skinlist = []
        for i in skinidlist:
            tmpSkin = {
                'skinID': i.skinID,
                'skinsName': i.skinName,
                'description': i.description,
                'skinsValue': i.value,
                'isInStore': i.isInStore
            }
            skinlist.append(tmpSkin)
        response['skinlist'] = skinlist

    return jsonify(response)

@app.route('/api/props/user/<account>')
@login_required
def getUserProps(account):
    response = {
        'code': 1,
        'proplist': None
    }
    propidlist = User_Props.query.filter_by(account=account).all()

    if not propidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        proplist = []
        for i in propidlist:
            if i.propsNumber == 0:
                continue;
            tmpProp = {
                'propsID': i.propsID,
                'propsName': i.propMsg.propsName,
                'description': i.propMsg.description,
                'propsValue': i.propMsg.value,
                'isInStore': i.propMsg.isInStore,
                'propsNumber': i.propsNumber
            }
            proplist.append(tmpProp)
        response['proplist'] = proplist

    return jsonify(response)

@app.route('/api/props/all')
@login_required
def getPropsAll():
    response = {
        'code': 1,
        'proplist': None
    }
    propidlist = Prop.query.all()

    if not propidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        proplist = []
        for i in propidlist:
            tmpProp = {
                'propsID': i.propsID,
                'propsName': i.propsName,
                'description': i.description,
                'propsValue': i.value,
                'isInStore': i.isInStore
            }
            proplist.append(tmpProp)
        response['proplist'] = proplist

    return jsonify(response)

@app.route('/api/props/store')
@login_required
def getPropsInstore():
    response = {
        'code': 1,
        'proplist': None
    }
    propidlist = Prop.query.filter_by(isInStore=True).all()

    if not propidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        proplist = []
        for i in propidlist:
            tmpProp = {
                'propsID': i.propsID,
                'propsName': i.propsName,
                'description': i.description,
                'propsValue': i.value,
                'isInStore': i.isInStore
            }
            proplist.append(tmpProp)
        response['proplist'] = proplist

    return jsonify(response)

@app.route('/api/useProp', methods=['POST'])
@login_required
@require('account', 'propsId')
def useProp():
    response = {
        'code': 2
    }
    m_account = request.json.get('account',None)
    m_propsId = request.json.get('propsId',None)
    useprop = User_Props.query.filter_by(propsID=m_propsId,account=m_account).first()

    if not useprop or useprop.propsNumber == 0:
        response['code'] = 1
    else:
        useprop.propsNumber -= 1
        db.session.commit()
        response['code'] = 0

    return jsonify(response)

@app.route('/api/purchase', methods=['POST'])
@login_required
@require('account', 'goodId', 'goodNum', 'type')
def buyGood():
    response = {
        'code': 4
    }
    m_account = request.json.get('account',None)
    m_type = request.json.get('type',None)
    m_goodId = int(request.json.get('goodId',None))
    m_goodNum = int(request.json.get('goodNum',None))

    purchaseUsr = User.query.get(m_account)
    if not purchaseUsr:
        return jsonify(response)

    purchaseGood = None
    if m_type == 'props':
        purchaseGood = Prop.query.get(m_goodId)
    elif m_type == 'skin':
        m_goodNum = 1
        purchaseGood = Skin.query.get(m_goodId)
    else:
        return jsonify(response)

    if not purchaseGood or purchaseGood.isInStore == False:
        response['code'] = 3
    elif purchaseGood.value * m_goodNum > purchaseUsr.goalCoin:
        response['code'] = 1
    else:
        userGoodMsg = None
        if m_type == 'props':
            userGoodMsg = User_Props.query.filter_by(propsID=m_goodId,account=m_account).first()
            if not userGoodMsg:
                userGoodMsg = User_Props(account=m_account, propsID=m_goodId, propsNumber=m_goodNum)
            else:
                userGoodMsg.propsNumber += m_goodNum
        elif m_type == 'skin':
            userGoodMsg = User_Skins.query.filter_by(skinID=m_goodId,account=m_account).first()
            if not userGoodMsg:
                userGoodMsg = User_Skins(account=m_account, skinID=m_goodId)
            else:
                response['code'] = 2
                return jsonify(response)
        purchaseUsr.goalCoin -= purchaseGood.value * m_goodNum
        db.session.add(userGoodMsg)
        db.session.commit()
        response['code'] = 0

    return jsonify(response)
