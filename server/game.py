from flask import jsonify, request
from flask_login import login_required
from server import db, app
from .Handler.hd_base import require
from .models import User, Game_Version, Level, User_LevelRecord

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

@app.route('/api/gameRecord/<account>/<levelid>', methods=['POST'])
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
    record = User_LevelRecord.query.filter_by(account=account, levelID=levelid).first()

    if not record:
        response['code'] = 0
        record = User_LevelRecord(levelID=levelid, account=account, record_time=m_time)
    elif record.record_time > m_time:
        response['code'] = 0
        record.record_time = m_time
    else:
        response['code'] = 1

    if record.levelsMsg.skinMsg:
        response['skinName'] = record.levelsMsg.skinMsg.skinName

    if record.levelsMsg.propMsg:
        response['propsName'] = record.levelsMsg.propMsg.propsName

    if record.levelsMsg.levelGold != 0:
        response['levelGold'] = record.levelsMsg.levelGold
    db.session.add(record)
    db.session.commit()

    return jsonify(response)


# @app.route('/api/gameVersions/all')
# @login_required
# def getGameVersionsAll():
# response = {
#     'code': 1,
#     'gmvrslist': None
# }
# levelidlist = Level.query.all()
#
# if not levelidlist:
#     response['code'] = 0
# else:
#     response['code'] = 0
#     levellist = []
#     for i in levelidlist:
#         tmpLevel = {
#             'levelID': i.levelID,
#             'levelName': i.levelName,
#             'difficulty': i.difficulty,
#             'mapMsg': {
#                 'mapID': i.mapMsg.mapID,
#                 'mapName': i.mapMsg.mapName,
#                 'description': i.mapMsg.description
#             }
#         }
#         levellist.append(tmpLevel)
#     response['levellist'] = levellist
#
# return jsonify(response)
