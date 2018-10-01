# 后端设计

### 数据库设计

##### 用户表
用户基本信息表

|  属性名 |  数据类型  |  键  |    描述    |
| ------- | --------- | ---- | --------- |
| account |  Integer  | 主键 |  用户账号  |
| nickname|   String  |  -   |  用户昵称  |
|   mail  |   String  |  -   |  用户邮箱  |
| password|   String  |  -   |  用户密码  |
| goalCoin|  Integer  |  -   |用户金币数量|

用户获得消耗道具表

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  account  |  Integer  | 外键 |  用户账号  |
|  propsID  |  Integer  | 外键 | 游戏道具ID |
|propsNumber|  Integer  |  -   |获得道具数量|

用户获得皮肤表

|  属性名 |  数据类型  |  键  |    描述    |
| ------- | --------- | ---- | --------- |
| account |  Integer  | 外键 |  用户账号  |
|  skinID |  Integer  | 外键 | 游戏皮肤ID |

道具表

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  propsID  |  Integer  | 主键 |   道具ID   |
| propsName |   String  |   -  |  道具名称  |
|description|   String  |   -  |  道具描述  |
| propsValue|  Integer  |   -  |  道具价值  |
| isInStore |  Boolean  |   -  |是否放入商场|

皮肤表

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

地图信息表

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|   mapID   |   Integer | 主键 |   地图ID   |
|  mapName  |   String  |   -  |  地图名称  |
|description|   String  |   -  |  地图描述  |
| startPosX |  Integer  |   -  |  起点X位置 |
| startPosY |  Integer  |   -  |  起点Y位置 |
|  endPosX  |  Integer  |   -  |  终点X位置 |
|  endPosY  |  Integer  |   -  |  终点Y位置 |

地图属性表

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|   mapID   |  Integer  | 外键 |   地图ID   |
|  propsID  |  Integer  | 外键 |   道具ID   |
| propsPosX |  Integer  |   -  |  道具X位置 |
| propsPosY |  Integer  |   -  |  道具Y位置 |

关卡信息表

|   属性名  |  数据类型  |  键  |    描述    |
| --------- | --------- | ---- | --------- |
|  levelID  |   String  | 主键 |   关卡ID   |
| levelName |   String  |   -  |  关卡名称  |
|   mapID   |   Integer | 外键 |关卡使用地图ID|
|  easyTime |   Integer |   -  |简单过关秒数|
| middleTime|   Integer |   -  |中等过关秒数|
|difficultTime| Integer |   -  |困难过关秒数|
|  propsID  |  Integer  | 外键 |过关获得道具ID|
|  skinID   |  Integer  | 外键 |过关获得皮肤ID|
| levelGold |  Integer  |   -  |过关获得金币数量|

用户通关记录表

|  属性名 |  数据类型  |  键  |    描述    |
| ------- | --------- | ---- | --------- |
| account |  Integer  | 外键 |  用户账号  |
| levelID |  Integer  | 外键 |   关卡ID   |
|   time  |  Integer  |  -   |通关时间秒数|

### 接口设计
