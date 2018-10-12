from server import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    account = db.Column(db.String(12), primary_key=True)
    nickname = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    goalCoin = db.Column(db.Integer, default=0)

    def __init__(self, account, nickname, mail, password):
        self.account = account
        self.nickname = nickname
        self.mail = mail
        self.password = password

    #flask_login需要的4个验证方式
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.account

    def __repr__(self):
        user = '<User> '
        user += 'account: %r\n' % (self.account)
        user += 'nickname: %r\n' % (self.nickname)
        user += 'mail: %r\n' % (self.mail)
        return user

class Props(db.Model):
    #__bind_key__ = 'xnet_master'
    __tablename__ = 'props'

    propsID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    propsname = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255))
    propsValue = db.Column(db.Integer, nullable=False)
    isInStore = db.Column(db.Boolean, default=False)

    def __init__(self, propsname, description, propsValue, isInStore):
        self.propsname = propsname
        self.description = description
        self.propsValue = propsValue
        self.isInStore = isInStore

    def __repr__(self):
        props = '<Props> '
        props += 'propsID: %r\n' % (self.propsID)
        props += 'propsname: %r\n' % (self.propsname)
        props += 'description: %r\n' % (self.description)
        props += 'propsValue: %r\n' % (self.propsValue)
        props += 'isInStore: %r\n' % (self.isInStore)
        return props

class User_Props(db.Model):
    __tablename__ = 'users_props'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(12), db.ForeignKey('users.account'), nullable=False)
    propsID = db.Column(db.Integer, db.ForeignKey('props.propsID'), nullable=False)
    propsNumber = db.Column(db.Integer, nullable=False)

    def __init__(self, account, propsID, propsNumber):
        self.account = account
        self.propsID = propsID
        self.propsNumber = propsNumber

    def __repr__(self):
        user_props = '<User_Props> '
        user_props += 'id: %r\n' % (self.id)
        user_props += 'account: %r\n' % (self.account)
        user_props += 'propsID: %r\n' % (self.propsID)
        user_props += 'propsNumber: %r\n' % (self.propsNumber)
        return user_props

class Skin(db.Model):
    #__bind_key__ = 'xnet_master'
    __tablename__ = 'skins'

    skinID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skinsname = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255))
    skinsValue = db.Column(db.Integer, nullable=False)
    isInStore = db.Column(db.Boolean, default=False)
    weight = db.Column(db.Integer, nullable=False)
    elasticity = db.Column(db.Integer, nullable=False)
    roughness = db.Column(db.Integer, nullable=False)
    maxSpeed = db.Column(db.Integer, nullable=False)

    def __init__(self, skinsname, description, skinsValue, isInStore,
                  weight, elasticity, roughness, maxSpeed):
        self.skinsname = skinsname
        self.skinsValue = skinsValue
        self.description = description
        self.isInStore = isInStore
        self.weight = weight
        self.elasticity = elasticity
        self.roughness = roughness
        self.maxSpeed = maxSpeed

    def __repr__(self):
        skin = '<Skin> '
        skin += 'skinID: %r\n' % (self.skinID)
        skin += 'skinsname: %r\n' % (self.skinsname)
        skin += 'skinsValue: %r\n' % (self.skinsValue)
        skin += 'isInStore: %r\n' % (self.isInStore)
        return skin

class User_Skins(db.Model):
    __tablename__ = 'user_skins'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(12), db.ForeignKey('users.account'), nullable=False)
    skinID = db.Column(db.Integer, db.ForeignKey('skins.skinID'), nullable=False)

    def __init__(self, account, skinID):
        self.account = account
        self.skinID = skinID

    def __repr__(self):
        user_skins = '<user_skins> '
        user_skins += 'id: %r\n' % (self.id)
        user_skins += 'account: %r\n' % (self.account)
        user_skins += 'skinID: %r\n' % (self.skinID)
        return user_skins

class Game_Version(db.Model):
    __tablename__ = 'game_version'

    versionNum = db.Column(db.String(11), primary_key=True)
    update_time = db.Column(db.TIMESTAMP(), nullable=False)

    def __init__(self, versionNum, update_time):
        self.versionNum = versionNum
        self.update_time = update_time

    def __repr__(self):
        game_version = '<game_version> '
        game_version += 'versionNum: %r\n' % (self.versionNum)
        game_version += 'update_time: %r\n' % (self.update_time)
        return game_version

class Map(db.Model):
    __tablename__ = 'maps'

    mapID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mapName = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255))

    def __init__(self, mapName, description):
        self.mapName = mapName
        self.description = description

    def __repr__(self):
        map = '<Map> '
        map += 'mapID: %r\n' % (self.mapID)
        map += 'mapName: %r\n' % (self.mapName)
        map += 'description: %r\n' % (self.description)
        return map

class Level(db.Model):
    __tablename__ = 'levels'

    levelID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    levelName = db.Column(db.String(20), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    mapID = db.Column(db.Integer, db.ForeignKey('maps.mapID'), nullable=False)
    skinID = db.Column(db.Integer, db.ForeignKey('skins.skinID'))
    propsID = db.Column(db.Integer, db.ForeignKey('props.propsID'))
    levelGold = db.Column(db.Integer, default=0)
    easy_time = db.Column(db.Integer, nullable=False)
    startPosX = db.Column(db.Integer, nullable=False)
    startPosY = db.Column(db.Integer, nullable=False)
    startPosZ = db.Column(db.Integer, nullable=False)
    endPosX = db.Column(db.Integer, nullable=False)
    endPosY = db.Column(db.Integer, nullable=False)
    endPosZ = db.Column(db.Integer, nullable=False)

    def __init__(self, levelName, difficulty, mapID, skinID, propsID,
    levelGold, easy_time, startPosX, startPosY, startPosZ, endPosX, endPosY, endPosZ):
        self.levelName = levelName
        self.difficulty = difficulty
        self.mapID = mapID
        self.skinID = skinID
        self.propsID = propsID
        self.levelGold = levelGold
        self.easy_time = easy_time
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.startPosZ = startPosZ
        self.endPosX = endPosX
        self.endPosY = endPosY
        self.endPosZ = endPosZ

    def __repr__(self):
        level = '<Level> '
        level += 'levelID: %r\n' % (self.levelID)
        level += 'levelName: %r\n' % (self.levelName)
        level += 'difficulty: %r\n' % (self.difficulty)
        level += 'mapID: %r\n' % (self.mapID)
        level += 'skinID: %r\n' % (self.skinID)
        level += 'propsID: %r\n' % (self.propsID)
        level += 'levelGold: %r\n' % (self.levelGold)
        return level

class Level_Props(db.Model):
    __tablename__ = 'levels_props'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    levelID = db.Column(db.Integer, db.ForeignKey('levels.levelID'), nullable=False)
    propsID = db.Column(db.Integer, db.ForeignKey('props.propsID'), nullable=False)
    propsPosX = db.Column(db.Integer, nullable=False)
    propsPosY = db.Column(db.Integer, nullable=False)
    propsPosZ = db.Column(db.Integer, nullable=False)

    def __init__(self, levelID, propsID, propsPosX, propsPosY, propsPosZ):
        self.levelID = levelID
        self.propsID = propsID
        self.propsPosX = propsPosX
        self.propsPosY = propsPosY
        self.propsPosZ = propsPosZ

    def __repr__(self):
        levels_props = '<Level_Props> '
        levels_props += 'id: %r\n' % (self.id)
        levels_props += 'levelID: %r\n' % (self.levelID)
        levels_props += 'propsID: %r\n' % (self.propsID)
        levels_props += 'propsPosX: %r\n' % (self.propsPosX)
        levels_props += 'propsPosY: %r\n' % (self.propsPosY)
        levels_props += 'propsPosZ: %r\n' % (self.propsPosZ)
        return levels_props


class User_LevelRecord(db.Model):
    __tablename__ = 'users_levelRecord'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    levelID = db.Column(db.Integer, db.ForeignKey('levels.levelID'), nullable=False)
    account = db.Column(db.String(12), db.ForeignKey('users.account'), nullable=False)
    record_time = db.Column(db.Integer, nullable=False)

    def __init__(self, levelID, account, record_time):
        self.levelID = levelID
        self.account = account
        self.record_time = record_time

    def __repr__(self):
        users_levelRecord = '<Level_Props> '
        users_levelRecord += 'id: %r\n' % (self.id)
        users_levelRecord += 'levelID: %r\n' % (self.levelID)
        users_levelRecord += 'account: %r\n' % (self.account)
        users_levelRecord += 'record_time: %r\n' % (self.record_time)
        return users_levelRecord
