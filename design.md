# 后端设计

### 数据库设计

##### 用户表
用户基本信息表 users

> 存储位置： 服务器

|  属性名 |  数据类型  |  键  |    描述    |
| ------- | --------- | ---- | --------- |
| account |   String  | 主键 |  用户账号  |
| nickname|   String  |  -   |  用户昵称  |
|   mail  |   String  |  -   |  用户邮箱  |
| password|   String  |  -   |  用户密码  |
| goalCoin|  Integer  |  -   |用户金币数量|

用户获得消耗道具表 users_props

> 存储位置： 服务器

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  account  |  Integer  | 外键 |  用户账号  |
|  propsID  |  Integer  | 外键 | 游戏道具ID |
|propsNumber|  Integer  |  -   |获得道具数量|

用户获得皮肤表 users_skins

> 存储位置： 服务器

|  属性名 |  数据类型  |  键  |    描述    |
| ------- | --------- | ---- | --------- |
| account |  Integer  | 外键 |  用户账号  |
|  skinID |  Integer  | 外键 | 游戏皮肤ID |

道具表  props

> 存储位置： 本地（存储ue4设定包等资源类文件）、服务器（存储展示数据）

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  propsID  |  Integer  | 主键 |   道具ID   |
| propsName |   String  |   -  |  道具名称  |
|description|   String  |   -  |  道具描述  |
| propsValue|  Integer  |   -  |  道具价值  |
| isInStore |  Boolean  |   -  |是否放入商场|

皮肤表 skins

> 存储位置： 本地（存储ue4设定包等资源类文件）、服务器（存储展示数据）

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  skinID   |  Integer  | 主键 |   皮肤ID   |
| skinName  |   String  |   -  |  皮肤名称  |
|description|   String  |   -  |  皮肤描述  |
| skinValue |  Integer  |   -  |  皮肤价值  |
| isInStore |  Boolean  |   -  |是否放入商场|
|   weight  |  Integer  |   -  |    重量    |
| elasticity|  Integer  |   -  |    弹力    |
| roughness |  Integer  |   -  |  粗糙程度  |
|  maxSpeed |  Integer  |   -  |  最大速度  |

地图信息表 maps

> 存储位置： 本地（存储ue4设定包等资源类文件）、服务器（存储展示数据）

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|   mapID   |   Integer | 主键 |   地图ID   |
|  mapName  |   String  |   -  |  地图名称  |
|description|   String  |   -  |  地图描述  |

关卡信息表 levels

> 存储位置： 本地（存储ue4设定包等资源类文件）、服务器（存储展示数据）

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  levelID  |   String  | 主键 |   关卡ID   |
| difficulty|   Integer |   -  |  关卡难度  |
| levelName |   String  |   -  |  关卡名称  |
|   mapID   |   Integer | 外键 |关卡使用地图ID|
| easy_time |   Integer |   -  |简单过关秒数|
|  propsID  |  Integer  | 外键 |过关获得道具ID|
|  skinID   |  Integer  | 外键 |过关获得皮肤ID|
| levelGold |  Integer  |   -  |过关获得金币数量|
| startPosX |  Integer  |   -  |  起点X位置 |
| startPosY |  Integer  |   -  |  起点Y位置 |
| startPosZ |  Integer  |   -  |  起点Z位置 |
|  endPosX  |  Integer  |   -  |  终点X位置 |
|  endPosY  |  Integer  |   -  |  终点Y位置 |
|  endPosZ  |  Integer  |   -  |  终点Z位置 |

关卡道具表 levels_props

> 存储位置： 服务器（暂定）

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  levelID  |  Integer  | 外键 |   关卡ID   |
|  propsID  |  Integer  | 外键 |   道具ID   |
| propsPosX |  Integer  |   -  |  道具X位置 |
| propsPosY |  Integer  |   -  |  道具Y位置 |
| propsPosZ |  Integer  |   -  |  道具Z位置 |

用户通关记录表 users_levelRecord

> 存储位置： 服务器（存储展示数据）

|  属性名 |  数据类型  |  键  |    描述    |
| ------- | --------- | ---- | --------- |
| account |  Integer  | 外键 |  用户账号  |
| levelID |  Integer  | 外键 |   关卡ID   |
|record_time|Integer  |  -   |通关时间秒数|

游戏版本号 game_version

> 存储位置： 本地（存储ue4设定包等资源类文件）、服务器（存储展示数据）

|  属性名  |  数据类型  |  键  |    描述    |
| -------- | --------- | ---- | --------- |
|versionNum|   String  | 主键 |   版本号   |
|update_time|    Date  |   -  |版本更新时间|

### 接口设计

### 用户相关
#### 用户注册 ~
接口地址: /api/newAccount

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                   说明                        |
| ---- | ------- | ------- | ------- | -------------------------------------------- |
| 请求 |  account | String |    Y    |               用户账号(手机号)                 |
| 请求 | nickname | String |    Y    |             用户名(长度限制3-8位)              |
| 请求 | password | String |    Y    |            用户密码(长度限制8-12位)             |
| 请求 |   mail   | String |    Y    |                  用户邮箱                      |
| 应答 |   code   |  int   |    Y    | 返回注册结果，0成功，1手机号已被注册，其他系统错误|

json示例:

| 类型 |                                     json                                                 |
| ---- | ---------------------------------------------------------------------------------------- |
| 请求 |{"account":"13000000000","nickname":"111","password":"12345678", "mail":"12345678@qq.com"}|
| 应答 |                                   {"code":0}                                             |

#### 用户登录 ~
接口地址: /api/login

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 请求 |  account | String |    Y    |                   登录账号                     |
| 请求 | password | String |    Y    |                   用户密码                     |
| 应答 |   code   |  int   |    Y    |返回登录结果，0成功，1无此用户，2密码错误，3其他系统错误|
| 应答 | nickname | String |    Y    |               成功登录返回用户昵称              |
| 应答 | goalCoin | Integer|    Y    |              成功登录返回用户金币数             |

json示例:

| 类型 |                json                      |
| ---- | ---------------------------------------- |
| 请求 |{"account":"000000", "password":"12345678"}|
| 应答 |{"code":0", nickname":"ccc", "goalCoin":"0"}|

#### 用户登出 ~
接口地址: /api/logout

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 请求 |  account | String |    Y    |                   登出账号                     |
| 应答 |   code   |  int   |    Y    |           返回登出结果，0成功，1登出失败         |

json示例:

| 类型 |               json                     |
| ---- | -------------------------------------- |
| 请求 |         {"account":"000000"}           |
| 应答 |             {"code":0"}                |

## 皮肤道具相关
### 查询用户拥有皮肤 ~
接口地址: /api/skins/user/:account

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 应答 |   code   |  int   |    Y    |      返回询问结果，0查询状态成功，1出现错误       |
| 应答 | skinlist |SkinsArr|    Y    |                返回用户获得皮肤表               |

json示例:

| 类型 |           json          |
| ---- | ----------------------- |
| 应答 |{"code":0, "skinlist":[{"skinID": "001","skinName": "ppa","description": "it's ppa.","skinValue": "0","isInStore": "false","weight": "1","elasticity": "8","roughness": "2","maxSpeed": "5"}, {"skinID": "001","skinName": "ppb","description": "it's ppb.","skinValue": "2","isInStore": "true","weight": "2","elasticity": "3","roughness": "5","maxSpeed": "7"}]}|

### 查询用户拥有道具 ~
接口地址: /api/props/user/:account

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 应答 |   code   |  int   |    Y    |      返回询问结果，0查询状态成功，1出现错误       |
| 应答 | proplist |PropsArr|    Y    |                返回用户获得道具表               |

json示例:

| 类型 |           json          |
| ---- | ----------------------- |
| 应答 |{"code":0, "proplist":[{"propsID": "001","propsName": "sjk","description": "it's sjk.","propsValue": "0","isInStore": "false","propsNumber": "1"}, {"propsID": "002","propsName": "jsk","description": "it's jsk.","propsValue": "10","isInStore": "true","propsNumber": "5"}]}|

### 查询商城出售皮肤 ~
接口地址: /api/skins/store

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 应答 |   code   |  int   |    Y    |      返回询问结果，0查询状态成功，1出现错误       |
| 应答 | skinlist |SkinsArr|    Y    |                返回商城出售皮肤表               |

json示例:

| 类型 |           json          |
| ---- | ----------------------- |
| 应答 |{"code":0, "skinlist":[{"skinID": "001","skinName": "ppa","description": "it's ppa.","skinValue": "0","isInStore": "false","weight": "1","elasticity": "8","roughness": "2","maxSpeed": "5"}, {"skinID": "001","skinName": "ppb","description": "it's ppb.","skinValue": "2","isInStore": "true","weight": "2","elasticity": "3","roughness": "5","maxSpeed": "7"}]}|

### 查询商城出售道具 ~
接口地址: /api/props/store

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 应答 |   code   |  int   |    Y    |      返回询问结果，0查询状态成功，1出现错误       |
| 应答 | proplist |PropsArr|    Y    |                返回商城出售道具表               |

json示例:

| 类型 |           json          |
| ---- | ----------------------- |
| 应答 |{"code":0, "proplist":[{"propsID": "001","propsName": "sjk","description": "it's sjk.","propsValue": "0","isInStore": "true"}, {"propsID": "002","propsName": "jsk","description": "it's jsk.","propsValue": "10","isInStore": "true"}]}|

### 用户购买道具或皮肤 ~
接口地址: /api/purchase

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 请求 |  account | String |    Y    |                   购买账号                     |
| 请求 |   type   | String |    Y    |            购买商品类型'skin'、'props'          |
| 请求 |  goodId  | Integer|    Y    |                  购买商品id                    |
| 请求 | goodNum  | Integer|    Y    |                 购买商品数量                   |
| 应答 |   code   | Integer|    Y    |  返回购买结果，0购买成功，1金币不足，2重复购买皮肤,3无此物品，其他系统错误  |

json示例:

| 类型 |           json          |
| ---- | ----------------------- |
| 请求 |{"account":"000000", "type":"props", "goodId":"001", "goodNum":3}|
| 应答 |{"code":0}|

### 用户使用道具 ~
接口地址: /api/useProp

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 请求 |  account | String |    Y    |                 使用道具账号                   |
| 请求 |  propsId | Integer|    Y    |                  使用道具id                    |
| 应答 |   code   | Integer|    Y    |  返回购买结果，0使用成功，1道具不足,其他系统错误  |

json示例:

| 类型 |           json          |
| ---- | ----------------------- |
| 请求 |{"account":"000000", "propsId":"001"}|
| 应答 |{"code":0}|

## 游戏相关
### 查询游戏关卡查询 ~
接口地址: /api/levels/all

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |   类型    | 是否必须 |                      说明                     |
| ---- | ------- | --------- | ------- | --------------------------------------------- |
| 应答 |   code   |  Integer |    Y    |       返回查询结果，0查询成功，其他查询失败       |
| 应答 |levellist |levelssArr|    Y    |                    返回关卡列表                |

json示例:

| 类型 |                          json                        |
| ---- | ---------------------------------------------------- |
| 应答 |{"code":0, "levellist":[{levelID: 1,levelName: "level 1",difficulty: 1,mapMsg: {mapID: 1,mapName: 'map1',description: 'this is map1'}}, {levelID: 2,levelName: "level 2",difficulty: 3,mapMsg: {mapID: 2,mapName: 'map2',description: 'this is map2'}}]}|

### 查询用户通过游戏关卡进度 ~
接口地址: /api/levels/user/:account

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 应答 |   code   |  Integer |    Y    |       返回查询结果，0查询成功，其他查询失败    |
| 应答 |levellist |levelssArr|    Y    |                 返回通过关卡列表              |

json示例:

| 类型 |                          json                        |
| ---- | ---------------------------------------------------- |
| 应答 |{"code":0, "levellist":[{levelID: 1,levelName: "level 1",difficulty: 1,mapMsg: {mapID: 1,mapName: 'map1',description: 'this is map1'}, time:60}]}|

### 查询单个关卡具体信息 ~
接口地址: /api/level/:levelid

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | -------------------------------------------- |
| 应答 |   code   | Integer |    Y    |       返回查询结果，0查询成功，其他查询失败     |
| 应答 | levelMsg |levelItem|    Y    |                 返回单个关卡信息              |

json示例:

| 类型 |                          json                        |
| ---- | ---------------------------------------------------- |
| 应答 |{"code":0, "levelMsg":{levelID: 1,levelName: 'level1',difficulty: 1,mapMsg: {mapID: 1,mapName: 'map1',description: 'this is map1'}, skinMsg: {skinID: 2,skinName: 'skin2',description: 'this is skin2'},propsMsg: {propsID: 1,propsName: 'prop1',description: 'this is prop1'},levelGold: 5,easy_time: 60,startPosX: 0,startPosY: 0,startPosZ: 99,endPosX: 99,endPosY: 99,endPosZ: 99}}|

### 用户通关记录
接口地址: /api/gameRecord/:account/:levelid

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 请求 |   time   |  Integer |    Y    |                 通关花费时间                 |
| 应答 |   code   |  Integer |    Y    |  返回查询结果，0新纪录，1非新纪录，其他更改失败 |
| 应答 | propsName|  Integer |    Y    |                通关获得道具名称              |
| 应答 | skinName |  Integer |    Y    |                通关获得皮肤名称              |
| 应答 | levelGold|  Integer |    Y    |                  通关获得金币                |

json示例:

| 类型 |    json    |
| ---- | ---------- |
| 请求 |{"time": 48}|
| 应答 |{"code":  0, 'propsName': 'prop1', 'skinName': None, 'levelGold': 5}|

### 获得金币、道具及皮肤
接口地址: /api/award/:account

请求方式: POST

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | --------------------------------------------- |
| 请求 |   type   | String |    Y    |      获得奖励类型'skin'、'props'、'goldcoin'    |
| 请求 |  goodId  | Integer|    N    |                 获得奖励id(金币不需要)          |
| 请求 | goodNum  | Integer|    Y    |                 获得奖励数量                   |
| 应答 |   code   | Integer|    Y    |  返回购买结果，0获取成功,其他系统错误  |

json示例:

| 类型 |                          json                        |
| ---- | ---------------------------------------------------- |
| 请求 |{"type":"skin", "goodId":"001", "goodNum":1}|
| 应答 |{"code":0}]}|

### 获得游戏版本
接口地址: /api/gameVersions/all

请求方式: GET

请求参数及返回值说明:

| 类型 |  参数名  |  类型   | 是否必须 |                      说明                     |
| ---- | ------- | ------- | ------- | -------------------------------------------- |
| 应答 |   code   | Integer|    Y    |       返回购买结果，0获取成功,其他系统错误       |
| 应答 | gmvrslist|GameVersionList|    Y    |       游戏版本号及更新时间列表           |

json示例:

| 类型 |                          json                        |
| ---- | ---------------------------------------------------- |
| 应答 |{"code":0, "gmvrslist":[{version: '1.0.1',updateTime: 'Mon, 15 Oct 2018 09:49:49 GMT'}]}|
