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
    propsValue INT(11) NOT NULL,
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
    skinValue INT(11) NOT NULL,
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
AUTO_INCREMENT=1;
-- INSERT INTO tb_name(field1,...) VALUES(value1,...);
