webpackJsonp([7],{"64zs":function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o={data:function(){return{gmvrslist:[]}},created:function(){var t=this;this.$http.get("/api/gameVersions/all").then(function(e){e.data.code?t.$message.error("查询失败"):t.gmvrslist=e.data.gmvrslist}).catch(function(e){console.log(e),t.$message.error("网络错误")})}},n={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticStyle:{height:"100%"}},[e("el-table",{attrs:{data:this.gmvrslist}},[e("el-table-column",{attrs:{prop:"version",label:"版本号"}}),this._v(" "),e("el-table-column",{attrs:{prop:"updateTime",label:"更新时间"}})],1)],1)},staticRenderFns:[]};var a=s("VU/8")(o,n,!1,function(t){s("TICt")},"data-v-501a689d",null);e.default=a.exports},"9IxF":function(t,e){},KG6V:function(t,e){},NHnr:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});s("tvR6");var o=s("qBF2"),n=s.n(o),a=s("7+uW"),r={name:"App",methods:{toSignup:function(){this.$router.push({path:"/Signup"})},toLogin:function(){this.$router.push({path:"/Login"})},Logout:function(){var t=this,e={account:this.$store.state.LogMsg.account};this.$http.post("/api/logout",e).then(function(e){if(e.data.code)t.$message.error("登出失败");else{t.$store.commit("setLogout",{isLog:!1,account:"",nickname:"",mail:"",coins:0}),t.$router.push({path:"/Login"})}}).catch(function(e){console.log(e),t.$message.error("网络错误"),t.$router.push({path:"/Login"})})}}},i={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{attrs:{id:"app"}},[s("v-layout",{staticClass:"app-layout"},[s("v-header",[s("v-row",{staticClass:"demo-row"},[s("v-col",{attrs:{span:"18"}},[s("p",{staticStyle:{color:"#ddd","font-size":"26px"}},[t._v("Traveling Ball Backend test page")])]),t._v(" "),s("v-col",{attrs:{span:"6"}},[t.$store.state.LogMsg.isLog?s("div",{staticStyle:{float:"right"}},[s("v-popover",{attrs:{placement:"bottom",title:t.$store.state.LogMsg.nickname,trigger:"hover"}},[s("v-button",{attrs:{type:"dashed",ghost:""}},[t._v(t._s(t.$store.state.LogMsg.nickname))]),t._v(" "),s("div",{attrs:{slot:"content"},slot:"content"},[s("v-row",[s("v-col",{attrs:{span:"12"}},[s("li",[t._v("account: ")])]),t._v(" "),s("v-col",{attrs:{span:"12"}},[s("span",{staticStyle:{"padding-left":"8px"}},[t._v(t._s(t.$store.state.LogMsg.account))])]),t._v(" "),s("v-col",{attrs:{span:"12"}},[s("li",[t._v("nickname: ")])]),t._v(" "),s("v-col",{attrs:{span:"12"}},[s("span",{staticStyle:{"padding-left":"8px"}},[t._v(t._s(t.$store.state.LogMsg.nickname))])]),t._v(" "),s("v-col",{attrs:{span:"12"}},[s("li",[t._v("goldcoins: ")])]),t._v(" "),s("v-col",{attrs:{span:"12"}},[s("span",{staticStyle:{"padding-left":"8px"}},[t._v(t._s(t.$store.state.LogMsg.coins))])])],1)],1)],1),t._v(" "),s("v-button",{attrs:{type:"dashed",ghost:""},on:{click:t.Logout}},[t._v("Logout")])],1):s("div",{staticStyle:{float:"right"}},[s("v-button",{attrs:{type:"dashed",ghost:""},on:{click:t.toLogin}},[t._v("Login")]),t._v(" "),s("v-button",{attrs:{type:"dashed",ghost:""},on:{click:t.toSignup}},[t._v("Signup")])],1)])],1)],1),t._v(" "),s("v-content",{staticClass:"app-content",staticStyle:{flex:"1"}},[s("div",{staticClass:"main"},[s("router-view")],1)])],1)],1)},staticRenderFns:[]};var l=s("VU/8")(r,i,!1,function(t){s("KG6V")},null,null).exports,c=s("Dd8w"),u=s.n(c),p=s("NYxO"),g=s("/ocq");a.default.use(p.a);var d=new p.a.Store({state:{LogMsg:{isLog:!1,account:"",nickname:"",coins:0}},mutations:{setLogMsg:function(t,e){t.LogMsg=e,sessionStorage.setItem("LogMsg_account",t.LogMsg.account),sessionStorage.setItem("LogMsg_nickname",t.LogMsg.nickname),sessionStorage.setItem("LogMsg_coins",t.LogMsg.coins)},setLogout:function(t,e){t.LogMsg=e,sessionStorage.removeItem("LogMsg_account"),sessionStorage.removeItem("LogMsg_nickname"),sessionStorage.removeItem("LogMsg_coins")},isLogin:function(t){t.LogMsg.isLog||(t.LogMsg.account=sessionStorage.getItem("LogMsg_account"),t.LogMsg.nickname=sessionStorage.getItem("LogMsg_nickname"),t.LogMsg.coins=parseInt(sessionStorage.getItem("LogMsg_coins")),t.LogMsg.account&&""!=t.LogMsg.account&&(t.LogMsg.isLog=!0))},goldCoinChange:function(t,e){t.LogMsg.coins+=e,sessionStorage.setItem("LogMsg_coins",t.LogMsg.coins)}}}),m=s("d/CE"),h=s("WPPn"),v=s("XkzK"),f=s("64zs");a.default.use(g.a),a.default.use(p.a);var _=[{path:"/",component:"Home",name:"home",children:[{path:"/user/props",component:m.default,name:"userProps"},{path:"/user/skins",component:h.default,name:"userSkins"},{path:"/user/levels",component:v.default,name:"userLevels"},{path:"/manage/props",component:m.default,name:"mngProps"},{path:"/manage/skins",component:h.default,name:"mngSkins"},{path:"/manage/levels",component:v.default,name:"mngLevels"},{path:"/manage/versions",component:f.default,name:"mngVersions"}]},{path:"/Level/:id",component:"tests/Levelitem",name:"levelitem"},{path:"/Signup",component:"Signup",name:"signup"},{path:"/Login",component:"Login",name:"login"},{path:"*",component:"NotFound",name:"404"}].map(function(t){return u()({},t,{component:function(){return s("mUJ2")("./"+t.component+".vue")}})}),$=new g.a({routes:_,mode:"history"});$.beforeEach(function(t,e,s){switch(d.commit("isLogin"),t.name){case"login":case"signup":break;case"home":d.state.LogMsg.isLog||s({path:"/Login",query:{redirect:t.fullPath}})}s()});var b=$,w=s("mtWM"),L=s.n(w),k=(s("zwDs"),s("p620")),S=s.n(k);a.default.use(n.a),a.default.use(n.a),a.default.use(S.a),a.default.use(p.a),a.default.prototype.$http=L.a,a.default.config.productionTip=!1,new a.default({el:"#app",router:b,store:d,components:{App:l},template:"<App/>"})},TICt:function(t,e){},WPPn:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o={data:function(){return{skinlist:[],btnStatus:!1,btnShow:"仅看商城"}},watch:{$route:function(t,e){var s=this,o="/api/skins";"mngSkins"==t.name?o+="/all":"userSkins"==t.name?o+="/user/"+this.$store.state.LogMsg.account:this.$router.push({path:"/"}),this.$http.get(o).then(function(t){t.data.code?s.$message.error("查询失败"):(s.skinlist=t.data.skinlist,null!=s.skinlist&&0!=s.skinlist.length||s.$message.warning("皮肤数量为0"))}).catch(function(t){console.log(t),s.$message.error("网络错误")})}},created:function(){var t=this,e="/api/skins";"userSkins"==this.$route.name?e+="/user/"+this.$store.state.LogMsg.account:e+="/all",this.$http.get(e).then(function(e){e.data.code?t.$message.error("查询失败"):(t.skinlist=e.data.skinlist,null!=t.skinlist&&0!=t.skinlist.length||t.$message.warning("皮肤数量为0"))}).catch(function(e){console.log(e),t.$message.error("网络错误")})},methods:{onBuy:function(t){var e=this,s={account:this.$store.state.LogMsg.account,type:"skin",goodId:t.skinID,goodNum:1};this.$http.post("/api/purchase",s).then(function(s){s.data.code?1==s.data.code?e.$message.error("金币不足"):2==s.data.code?e.$message.error("已购买该皮肤"):3==s.data.code?e.$message.error("该皮肤已下架"):e.$message.error("购买失败"):(e.$message.success("购买成功"),e.$store.commit("goldCoinChange",-t.skinsValue))}).catch(function(t){console.log(t),e.$message.error("网络错误")})},onChange:function(){var t=this,e="/api/skins";this.btnStatus?(this.btnShow="仅看商城",e+="/all"):(this.btnShow="查看全部",e+="/store"),this.btnStatus=!this.btnStatus,this.$http.post(e).then(function(e){e.data.code?t.$message.error("查询失败"):(t.skinlist=e.data.skinlist,null!=t.skinlist&&0!=t.skinlist.length||t.$message.warning("皮肤数量为0"))}).catch(function(e){console.log(e),t.$message.error("网络错误")})}}},n={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticStyle:{height:"100%"}},[s("el-table",{attrs:{data:t.skinlist}},[s("el-table-column",{attrs:{prop:"skinID",label:"id",width:"80"}}),t._v(" "),s("el-table-column",{attrs:{label:"皮肤名"},scopedSlots:t._u([{key:"default",fn:function(e){return[s("v-popover",{attrs:{placement:"bottom",title:e.row.skinsName,trigger:"hover"}},[s("el-button",{attrs:{type:"text"}},[t._v(t._s(e.row.skinsName))]),t._v(" "),s("div",{attrs:{slot:"content"},slot:"content"},[t._v("\n            "+t._s(e.row.description)+"\n          ")])],1)]}}])}),t._v(" "),s("el-table-column",{attrs:{prop:"skinsValue",label:"价值",width:"90"}}),t._v(" "),s("el-table-column",{attrs:{label:"是否出售",width:"150"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v("\n        "+t._s(e.row.isInStore+"")+"\n      ")]}}])}),t._v(" "),"userSkins"!=t.$route.name?s("el-table-column",{attrs:{label:"op",width:"140"},scopedSlots:t._u([{key:"default",fn:function(e){return[s("el-button",{attrs:{disabled:!e.row.isInStore,type:"text"},on:{click:function(s){t.onBuy(e.row)}}},[t._v("购买")])]}}])}):t._e()],1),t._v(" "),"userSkins"!=t.$route.name?s("el-button",{staticStyle:{margin:"12px"},on:{click:t.onChange}},[t._v(t._s(t.btnShow))]):t._e()],1)},staticRenderFns:[]};var a=s("VU/8")(o,n,!1,function(t){s("9IxF")},"data-v-4fa96cd6",null);e.default=a.exports},XOgf:function(t,e){},XkzK:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o={data:function(){return{levellist:[],req:[],getAward:{type:"skin",goodId:0,goodNum:0},options:[{value:"skin",label:"皮肤"},{value:"props",label:"道具"},{value:"goldcoin",label:"金币"}]}},watch:{$route:function(t,e){var s=this,o="/api/levels";"userLevels"==t.name?o+="/user/"+this.$store.state.LogMsg.account:o+="/all",this.$http.get(o).then(function(t){if(t.data.code)s.$message.error("查询失败");else for(var e in s.levellist=t.data.levellist,null!=s.levellist&&0!=s.levellist.length||s.$message.warning("关卡数量为0"),s.req.splice(0,s.req.length),s.levellist){s.req.push({time:0})}}).catch(function(t){console.log(t),s.$message.error("网络错误")})}},created:function(){var t=this,e="/api/levels";"userLevels"==this.$route.name?e+="/user/"+this.$store.state.LogMsg.account:e+="/all",this.$http.get(e).then(function(e){if(e.data.code)t.$message.error("查询失败");else for(var s in t.levellist=e.data.levellist,null!=t.levellist&&0!=t.levellist.length||t.$message.warning("关卡数量为0"),t.req.splice(0,t.req.length),t.levellist){t.req.push({time:0})}}).catch(function(e){console.log(e),t.$message.error("网络错误")})},methods:{onRecord:function(t,e){var s=this,o="/api/gameRecord/"+this.$store.state.LogMsg.account+"/"+e.levelID;null!=this.req[t].time&&""!=this.req[t].time&&0!=this.req[t].time||this.$message.error("通关时间不合法"),this.$http.post(o,this.req[t]).then(function(e){switch(e.data.code){case 0:s.$message.success("刷新记录");case 1:s.$store.commit("goldCoinChange",e.data.levelGold),s.req[t].time=0;break;default:s.$message.error("通关失败")}}).catch(function(t){console.log(t),s.$message.error("网络错误")})},onAward:function(){var t=this,e="/api/award/"+this.$store.state.LogMsg.account;this.$http.post(e,this.getAward).then(function(e){e.data.code?t.$message.error("获得道具/皮肤/金币失败"):t.$message.success("获得道具/皮肤/金币成功")}).catch(function(e){console.log(e),t.$message.error("网络错误")})},toLevelitem:function(t){this.$router.push({path:"/Level/"+t.levelID})}}},n={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticStyle:{height:"100%"}},[s("el-table",{attrs:{data:t.levellist}},[s("el-table-column",{attrs:{prop:"levelID",label:"id",width:"60"}}),t._v(" "),s("el-table-column",{attrs:{label:"关卡名"},scopedSlots:t._u([{key:"default",fn:function(e){return[s("v-popover",{attrs:{placement:"bottom",title:e.row.levelName,trigger:"hover"}},[s("el-button",{attrs:{type:"text"},on:{click:function(s){t.toLevelitem(e.row)}}},[t._v(t._s(e.row.levelName))]),t._v(" "),s("div",{attrs:{slot:"content"},slot:"content"},[s("p",[t._v("mapid: "+t._s(e.row.mapMsg.mapID))]),t._v(" "),s("p",[t._v("mapName: "+t._s(e.row.mapMsg.mapName))]),t._v(" "),s("p",[t._v("description: "+t._s(e.row.mapMsg.description))])])],1)]}}])}),t._v(" "),s("el-table-column",{attrs:{prop:"difficulty",label:"难度",width:"80"}}),t._v(" "),"userLevels"==t.$route.name?s("el-table-column",{attrs:{prop:"time",label:"记录",width:"80"}}):t._e(),t._v(" "),s("el-table-column",{attrs:{label:"op"},scopedSlots:t._u([{key:"default",fn:function(e){return[s("v-input-number",{attrs:{min:1,max:1e3},model:{value:t.req[e.$index].time,callback:function(s){t.$set(t.req[e.$index],"time",s)},expression:"req[scope.$index].time"}}),t._v(" "),s("el-button",{staticStyle:{margin:"0 12px"},attrs:{type:"text"},on:{click:function(s){t.onRecord(e.$index,e.row)}}},[t._v("通关")])]}}])})],1),t._v(" "),s("v-form",{staticStyle:{margin:"12px"},attrs:{direction:"inline"}},[s("v-form-item",{staticStyle:{width:"120px"},attrs:{label:"类型"}},[s("v-select",{staticStyle:{width:"56px"},attrs:{data:t.options},model:{value:t.getAward.type,callback:function(e){t.$set(t.getAward,"type",e)},expression:"getAward.type"}})],1),t._v(" "),"goldcoin"!=t.getAward.type?s("v-form-item",{staticStyle:{width:"150px"},attrs:{label:"id"}},[s("v-input-number",{attrs:{min:1,max:1e3},model:{value:t.getAward.goodId,callback:function(e){t.$set(t.getAward,"goodId",e)},expression:"getAward.goodId"}})],1):t._e(),t._v(" "),s("v-form-item",{staticStyle:{width:"150px"},attrs:{label:"数量"}},[s("v-input-number",{attrs:{min:1,max:1e3},model:{value:t.getAward.goodNum,callback:function(e){t.$set(t.getAward,"goodNum",e)},expression:"getAward.goodNum"}})],1),t._v(" "),s("v-form-item",{staticStyle:{width:"100px"}},[s("v-button",{attrs:{type:"primary"},on:{click:function(e){t.onAward()}}},[t._v("获得")])],1)],1)],1)},staticRenderFns:[]};var a=s("VU/8")(o,n,!1,function(t){s("oBK6")},"data-v-657ffe9a",null);e.default=a.exports},"d/CE":function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o={data:function(){return{proplist:[],btnStatus:!1,btnShow:"仅看商城"}},watch:{$route:function(t,e){var s=this,o="/api/props";"mngProps"==t.name?o+="/all":"userProps"==t.name?o+="/user/"+this.$store.state.LogMsg.account:this.$router.push({path:"/"}),this.$http.get(o).then(function(t){t.data.code?s.$message.error("查询失败"):(s.proplist=t.data.proplist,null!=s.proplist&&0!=s.proplist.length||s.$message.warning("道具数量为0"))}).catch(function(t){console.log(t),s.$message.error("网络错误")})}},created:function(){var t=this,e="/api/props";"userProps"==this.$route.name?e+="/user/"+this.$store.state.LogMsg.account:e+="/all",this.$http.get(e).then(function(e){e.data.code?t.$message.error("查询失败"):(t.proplist=e.data.proplist,null!=t.proplist&&0!=t.proplist.length||t.$message.warning("道具数量为0"))}).catch(function(e){console.log(e),t.$message.error("网络错误")})},methods:{onUse:function(t){var e=this,s={account:this.$store.state.LogMsg.account,propsId:t.row.propsID};this.$http.post("/api/useProp",s).then(function(s){s.data.code?e.$message.error("道具不足"):0==--t.row.propsNumber&&(e.proplist.splice(t.$index,1),null!=e.proplist&&0!=e.proplist.length||e.$message.warning("道具数量为0"))}).catch(function(t){console.log(t),e.$message.error("网络错误")})},onBuy:function(t){var e=this,s={account:this.$store.state.LogMsg.account,type:"props",goodId:t.propsID,goodNum:1};this.$http.post("/api/purchase",s).then(function(s){s.data.code?1==s.data.code?e.$message.error("金币不足"):3==s.data.code?e.$message.error("该道具已下架"):e.$message.error("购买失败"):(e.$message.success("购买成功"),e.$store.commit("goldCoinChange",-t.propsValue))}).catch(function(t){console.log(t),e.$message.error("网络错误")})},onChange:function(){var t=this,e="/api/props";this.btnStatus?(this.btnShow="仅看商城",e+="/all"):(this.btnShow="查看全部",e+="/store"),this.btnStatus=!this.btnStatus,this.$http.post(e).then(function(e){e.data.code?t.$message.error("查询失败"):(t.proplist=e.data.proplist,null!=t.proplist&&0!=t.proplist.length||t.$message.warning("道具数量为0"))}).catch(function(e){console.log(e),t.$message.error("网络错误")})}}},n={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticStyle:{height:"100%"}},[s("el-table",{attrs:{data:t.proplist}},[s("el-table-column",{attrs:{prop:"propsID",label:"id",width:"60"}}),t._v(" "),s("el-table-column",{attrs:{label:"道具名"},scopedSlots:t._u([{key:"default",fn:function(e){return[s("v-popover",{attrs:{placement:"bottom",title:e.row.propsName,trigger:"hover"}},[s("el-button",{attrs:{type:"text"}},[t._v(t._s(e.row.propsName))]),t._v(" "),s("div",{attrs:{slot:"content"},slot:"content"},[t._v("\n            "+t._s(e.row.description)+"\n          ")])],1)]}}])}),t._v(" "),s("el-table-column",{attrs:{prop:"propsValue",label:"价值",width:"90"}}),t._v(" "),s("el-table-column",{attrs:{label:"是否出售",width:"100"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v("\n        "+t._s(e.row.isInStore+"")+"\n      ")]}}])}),t._v(" "),"userProps"==t.$route.name?s("el-table-column",{attrs:{prop:"propsNumber",label:"数量",width:"90"}}):t._e(),t._v(" "),s("el-table-column",{attrs:{label:"op",width:"120"},scopedSlots:t._u([{key:"default",fn:function(e){return["userProps"==t.$route.name?s("el-button",{attrs:{type:"text"},on:{click:function(s){t.onUse(e)}}},[t._v("使用")]):s("el-button",{attrs:{disabled:!e.row.isInStore,type:"text"},on:{click:function(s){t.onBuy(e.row)}}},[t._v("购买")])]}}])})],1),t._v(" "),"userProps"!=t.$route.name?s("el-button",{staticStyle:{margin:"12px"},on:{click:t.onChange}},[t._v(t._s(t.btnShow))]):t._e()],1)},staticRenderFns:[]};var a=s("VU/8")(o,n,!1,function(t){s("XOgf")},"data-v-61e6705c",null);e.default=a.exports},mUJ2:function(t,e,s){var o={"./Home.vue":["lO7g",3],"./Login.vue":["xJsL",4,0],"./NotFound.vue":["YcJa",1,0],"./Signup.vue":["psOb",2,0],"./tests/Levelitem.vue":["f5Bq",5],"./tests/Levels.vue":["XkzK"],"./tests/Props.vue":["d/CE"],"./tests/Skins.vue":["WPPn"],"./tests/Versions.vue":["64zs"]};function n(t){var e=o[t];return e?Promise.all(e.slice(1).map(s.e)).then(function(){return s(e[0])}):Promise.reject(new Error("Cannot find module '"+t+"'."))}n.keys=function(){return Object.keys(o)},n.id="mUJ2",t.exports=n},oBK6:function(t,e){},tvR6:function(t,e){},zwDs:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.271fc7362dd6ad6d7f67.js.map