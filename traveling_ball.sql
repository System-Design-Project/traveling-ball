drop database if exists traveling_ball;
create database traveling_ball;
use traveling_ball;

CREATE TABLE users(
    account VARCHAR(12) NOT NULL,
    UNIQUE (account),
    nickname VARCHAR(32) COLLATE utf8_bin NOT NULL,
    mail VARCHAR(80),
    password VARCHAR(80) NOT NULL,
    goalCoin INT(11) DEFAULT 0,
    INDEX(account),
    PRIMARY KEY (account)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE props(
    propsID INT(11) NOT NULL AUTO_INCREMENT,
    propsName VARCHAR(20) NOT NULL,
    description VARCHAR(255),
    value INT(11) NOT NULL,
    isInStore BOOLEAN DEFAULT FALSE,
    INDEX(propsID),
    PRIMARY KEY (propsID)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE users_props(
    id INT(11) NOT NULL AUTO_INCREMENT,
    account VARCHAR(12) NOT NULL,
    propsID INT(11) NOT NULL,
    propsNumber INT(11) NOT NULL,
    INDEX(account),
    FOREIGN KEY (account) REFERENCES users(account) ON UPDATE CASCADE,
    FOREIGN KEY (propsID) REFERENCES props(propsID) ON UPDATE CASCADE,
    PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE skins(
    skinID INT(11) NOT NULL AUTO_INCREMENT,
    skinName VARCHAR(20) NOT NULL,
    description VARCHAR(255),
    value INT(11) NOT NULL,
    isInStore BOOLEAN DEFAULT FALSE,
    weight INT(11) NOT NULL,
    elasticity INT(11) NOT NULL,
    roughness INT(11) NOT NULL,
    maxSpeed INT(11) NOT NULL,
    INDEX(skinID),
    PRIMARY KEY (skinID)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE users_skins(
    id INT(11) NOT NULL AUTO_INCREMENT,
    account VARCHAR(12) NOT NULL,
    skinID INT(11) NOT NULL,
    INDEX(account),
    FOREIGN KEY (account) REFERENCES users(account) ON UPDATE CASCADE,
    FOREIGN KEY (skinID) REFERENCES skins(skinID) ON UPDATE CASCADE,
    PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE game_version(
    versionNum VARCHAR(11) NOT NULL,
    UNIQUE (versionNum),
    update_time timestamp COLLATE utf8_bin NOT NULL,
    INDEX(versionNum),
    PRIMARY KEY (versionNum)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE maps(
    mapID INT(11) NOT NULL AUTO_INCREMENT,
    mapName VARCHAR(20) NOT NULL,
    description VARCHAR(255),
    INDEX(mapID),
    PRIMARY KEY (mapID)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE levels(
    levelID INT(11) NOT NULL AUTO_INCREMENT,
    levelName VARCHAR(20) NOT NULL,
    difficulty INT(11) NOT NULL,
    mapID INT(11) NOT NULL,
    skinID INT(11),
    propsID INT(11),
    levelGold INT(11) DEFAULT 0,
    easy_time INT(11) NOT NULL,
    startPosX INT(11) NOT NULL,
    startPosY INT(11) NOT NULL,
    startPosZ INT(11) NOT NULL,
    endPosX INT(11) NOT NULL,
    endPosY INT(11) NOT NULL,
    endPosZ INT(11) NOT NULL,
    INDEX(levelID),
    FOREIGN KEY (propsID) REFERENCES props(propsID) ON UPDATE CASCADE,
    FOREIGN KEY (skinID) REFERENCES skins(skinID) ON UPDATE CASCADE,
    FOREIGN KEY (mapID) REFERENCES maps(mapID) ON UPDATE CASCADE,
    PRIMARY KEY (levelID)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE levels_props(
    id INT(11) NOT NULL AUTO_INCREMENT,
    levelID INT(11) NOT NULL,
    propsID INT(11),
    propsPosX INT(11) NOT NULL,
    propsPosY INT(11) NOT NULL,
    propsPosZ INT(11) NOT NULL,
    INDEX(levelID),
    FOREIGN KEY (propsID) REFERENCES props(propsID) ON UPDATE CASCADE,
    FOREIGN KEY (levelID) REFERENCES levels(levelID) ON UPDATE CASCADE,
    PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;

CREATE TABLE users_levelRecord(
    id INT(11) NOT NULL AUTO_INCREMENT,
    levelID INT(11) NOT NULL,
    account VARCHAR(12) NOT NULL,
    record_time INT(11) NOT NULL,
    INDEX(levelID),
    FOREIGN KEY (account) REFERENCES users(account) ON UPDATE CASCADE,
    FOREIGN KEY (levelID) REFERENCES levels(levelID) ON UPDATE CASCADE,
    PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin

-- AUTO_INCREMENT=1;
--
-- -- test data
-- INSERT INTO users(account,nickname,mail,password,goalCoin) VALUES('root','backendtest','12345678@qq.com','12345678',30);
-- INSERT INTO users(account,nickname,mail,password) VALUES('1512190210','1','87654321@qq.com','12345678');
--
-- INSERT INTO props(propsName,description,value,isInStore) VALUES('prop1','this is prop1',3,FALSE);
-- INSERT INTO props(propsName,description,value,isInStore) VALUES('prop2','this is prop2',2,TRUE);
-- INSERT INTO props(propsName,description,value,isInStore) VALUES('prop3','this is prop3',10,TRUE);
-- INSERT INTO props(propsName,description,value,isInStore) VALUES('prop4','this is prop4',40,TRUE);
--
-- INSERT INTO users_props(account,propsID,propsNumber) VALUES('root',2,1);
-- INSERT INTO users_props(account,propsID,propsNumber) VALUES('1512190210',1,5);
-- INSERT INTO users_props(account,propsID,propsNumber) VALUES('root',1,3);
--
-- INSERT INTO skins(skinName, description, value, isInStore, weight, elasticity, roughness, maxSpeed)
-- VALUES('skin1','this is skin1',5,TRUE,1,2,3,4);
-- INSERT INTO skins(skinName, description, value, isInStore, weight, elasticity, roughness, maxSpeed)
-- VALUES('skin2','this is skin3',10,FALSE,4,3,2,1);
-- INSERT INTO skins(skinName, description, value, isInStore, weight, elasticity, roughness, maxSpeed)
-- VALUES('skin3','this is skin3',30,TRUE,5,5,5,5);
--
-- INSERT INTO users_skins(account,skinID) VALUES('1512190210',1);
-- INSERT INTO users_skins(account,skinID) VALUES('root',1);
-- INSERT INTO users_skins(account,skinID) VALUES('root',2);
--
-- INSERT INTO maps(mapName, description) VALUES('map1','this is map1');
-- INSERT INTO maps(mapName, description) VALUES('map2','this is map2');
--
-- INSERT INTO levels(levelName,difficulty,mapID,skinID,levelGold,easy_time,startPosX,startPosY,
--   startPosZ,endPosX,endPosY,endPosZ) VALUES('level1',1,1,1,5,60,0,0,0,100,100,0);
-- INSERT INTO levels(levelName,difficulty,mapID,propsID,levelGold,easy_time,startPosX,startPosY,
--   startPosZ,endPosX,endPosY,endPosZ) VALUES('level2',3,2,3,10,48,0,1,0,100,100,0);
-- INSERT INTO levels(levelName,difficulty,mapID,skinID,propsID,levelGold,easy_time,startPosX,startPosY,
--   startPosZ,endPosX,endPosY,endPosZ) VALUES('level3',5,1,3,4,15,61,0,0,1,100,100,0);
--
-- INSERT INTO users_levelRecord(levelID,account,record_time) VALUES(1,'root',57);
--
-- INSERT INTO game_version(versionNum,update_time) VALUES('1.0.0', CURRENT_TIMESTAMP);
