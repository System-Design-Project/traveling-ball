from flask import jsonify, request
from flask_login import login_required
from server import db, app
from .Handler.hd_base import require
from .models import *

@app.route('/api/levels/user/<account>')
@login_required
def getUserLevels(account):
    response = {
        'code': 1,
        'levellist': None
    }
    levelidlist = User_LevelRecord.query.order_by(User_LevelRecord.levelID).filter_by(account=account).all()

    if not levelidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        levellist = []
        for i in levelidlist:
            tmpLevel = {
                'levelID': i.levelID,
                'levelName': i.levelsMsg.levelName,
                'difficulty': i.levelsMsg.difficulty,
                'mapMsg': {
                    'mapID': i.levelsMsg.mapMsg.mapID,
                    'mapName': i.levelsMsg.mapMsg.mapName,
                    'description': i.levelsMsg.mapMsg.description
                },
                'time': i.record_time
            }
            levellist.append(tmpLevel)
        response['levellist'] = levellist

    return jsonify(response)

@app.route('/api/level/<int:levelid>')
@login_required
def getLevelMsg(levelid):
    response = {
        'code': 1,
        'levelMsg': None
    }
    levelitem = Level.query.get(levelid)

    if levelitem:
        response['code'] = 0
        response['levelMsg'] = {
            'levelID': levelitem.levelID,
            'levelName': levelitem.levelName,
            'difficulty': levelitem.difficulty,
            'mapMsg': {
                'mapID': levelitem.mapMsg.mapID,
                'mapName': levelitem.mapMsg.mapName,
                'description': levelitem.mapMsg.description
            },
            'skinMsg': None,
            'propsMsg': None,
            'levelGold': levelitem.levelGold,
            'easy_time': levelitem.easy_time,
            'startPosX': levelitem.startPosX,
            'startPosY': levelitem.startPosY,
            'startPosZ': levelitem.startPosZ,
            'endPosX': levelitem.endPosX,
            'endPosY': levelitem.endPosY,
            'endPosZ': levelitem.endPosZ
        }
        if levelitem.propMsg:
            response['levelMsg']['propsMsg'] = {
               'propsID': levelitem.propMsg.propsID,
               'propsName': levelitem.propMsg.propsName,
               'description': levelitem.propMsg.description
            }
        if levelitem.skinMsg:
            response['levelMsg']['skinMsg'] = {
               'skinID': levelitem.skinMsg.skinID,
               'skinName': levelitem.skinMsg.skinName,
               'description': levelitem.skinMsg.description
            }

    return jsonify(response)

@app.route('/api/levels/all')
@login_required
def getLevelsAll():
    response = {
        'code': 1,
        'levellist': None
    }
    levelidlist = Level.query.all()

    if not levelidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        levellist = []
        for i in levelidlist:
            tmpLevel = {
                'levelID': i.levelID,
                'levelName': i.levelName,
                'difficulty': i.difficulty,
                'mapMsg': {
                    'mapID': i.mapMsg.mapID,
                    'mapName': i.mapMsg.mapName,
                    'description': i.mapMsg.description
                }
            }
            levellist.append(tmpLevel)
        response['levellist'] = levellist

    return jsonify(response)

@app.route('/api/gameRecord/<account>/<int:levelid>', methods=['POST'])
@login_required
@require('time')
def NewRecord(account, levelid):
    response = {
        'code': 2,
        'skinName': None,
        'propsName': None,
        'levelGold': 0
    }
    m_time = int(request.json.get('time',None))

    newRecordUsr = User.query.get(account)
    if not newRecordUsr:
        return jsonify(response)

    record = User_LevelRecord.query.filter_by(account=account, levelID=levelid).first()

    if not record:
        response['code'] = 0
        record = User_LevelRecord(levelID=levelid, account=account, record_time=m_time)
    elif record.record_time > m_time:
        response['code'] = 0
        record.record_time = m_time
    else:
        response['code'] = 1
    db.session.add(record)
    db.session.commit()

    if record.levelsMsg.skinID:
        response['skinName'] = record.levelsMsg.skinMsg.skinName
        addUsrSkin = User_Skins.query.filter_by(account=account,skinID=record.levelsMsg.skinID)
        if not addUsrSkin:
            addUsrSkin = User_Skins(account=account,skinID=record.levelsMsg.skinID)
            db.session.add(addUsrSkin)

    if record.levelsMsg.propsID:
        response['propsName'] = record.levelsMsg.propMsg.propsName
        addUsrProp = User_Props.query.filter_by(account=account, propsID=record.levelsMsg.propsID).first()
        if not addUsrProp:
            addUsrProp = User_Props(account=account, propsID=record.levelsMsg.propsID, propsNumber=1)
            db.session.add(addUsrProp)
        else:
            addUsrProp.propsNumber += 1

    if record.levelsMsg.levelGold != 0:
        response['levelGold'] = record.levelsMsg.levelGold
        newRecordUsr.goalCoin += record.levelsMsg.levelGold
    db.session.commit()

    return jsonify(response)

@app.route('/api/award/<account>', methods=['POST'])
@login_required
@require('goodNum', 'type')
def getAward(account):
    response = {
        'code': 1
    }
    m_type = request.json.get('type',None)
    m_goodId = int(request.json.get('goodId',None))
    m_goodNum = int(request.json.get('goodNum',None))

    newAwardUsr = User.query.get(account)
    if not newAwardUsr:
        return jsonify(response)

    if m_type == 'skin':
        if not Skin.query.get(m_goodId):
            return jsonify(response)
        addUsrSkin = User_Skins.query.filter_by(account=account,skinID=m_goodId)
        if not addUsrSkin:
            addUsrSkin = User_Skins(account=account,skinID=m_goodId)
            db.session.add(addUsrSkin)
        response['code'] = 0
    elif m_type == 'props':
        if not Prop.query.get(m_goodId):
            return jsonify(response)
        addUsrProp = User_Props.query.filter_by(account=account, propsID=m_goodId).first()
        if not addUsrProp:
            addUsrProp = User_Props(account=account, propsID=m_goodId, propsNumber=1)
            db.session.add(addUsrProp)
        else:
            addUsrProp.propsNumber += m_goodNum
        response['code'] = 0
    elif m_type == 'goldcoin':
        newAwardUsr.goalCoin += m_goodNum
        response['code'] = 0

    db.session.commit()

    return jsonify(response)

@app.route('/api/gameVersions/all')
@login_required
def getGameVersionsAll():
    response = {
        'code': 1,
        'gmvrslist': None
    }
    gvidlist = Game_Version.query.order_by(Game_Version.update_time.desc()).all()

    if not gvidlist:
        response['code'] = 0
    else:
        response['code'] = 0
        gvlist = []
        for i in gvidlist:
            tmpGv = {
                'version': i.versionNum,
                'updateTime': i.update_time
            }
            gvlist.append(tmpGv)
        response['gmvrslist'] = gvlist

    return jsonify(response)
