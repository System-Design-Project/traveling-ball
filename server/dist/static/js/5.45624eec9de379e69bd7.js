webpackJsonp([5],{D5xQ:function(e,s){},f5Bq:function(e,s,t){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var l={data:function(){return{levelMsg:{mapMsg:{mapID:0,mapName:"",description:""}}}},watch:{$route:function(e,s){var t=this,l="/api/level/"+this.$route.params.id;this.$http.get(l).then(function(e){e.data.code?t.$message.error("查询失败"):t.levelMsg=e.data.levelMsg}).catch(function(e){console.log(e),t.$message.error("网络错误")})}},created:function(){var e=this,s="/api/level/"+this.$route.params.id;this.$http.get(s).then(function(s){s.data.code?e.$message.error("查询失败"):e.levelMsg=s.data.levelMsg}).catch(function(s){console.log(s),e.$message.error("网络错误")})}},v={render:function(){var e=this,s=e.$createElement,t=e._self._c||s;return t("v-card",{staticClass:"levelitem-page",attrs:{title:e.levelMsg.levelID+". "+e.levelMsg.levelName}},[t("v-timeline",[t("v-timeline-item",{attrs:{color:"green"}},[e._v("难度： "+e._s(e.levelMsg.difficulty))]),e._v(" "),t("v-timeline-item",{attrs:{color:"green"}},[e._v("1星过关时间： "+e._s(e.levelMsg.easy_time))]),e._v(" "),t("v-timeline-item",{attrs:{color:"red"}},[t("v-collapse",{attrs:{bordered:!1}},[t("v-panel",{attrs:{header:"地图信息",index:"1"}},[t("p",[e._v("地图id: "+e._s(e.levelMsg.mapMsg.mapID))]),e._v(" "),t("p",[e._v("地图名称: "+e._s(e.levelMsg.mapMsg.mapName))]),e._v(" "),t("p",[e._v("描述: "+e._s(e.levelMsg.mapMsg.description))])])],1)],1),e._v(" "),t("v-timeline-item",[e._v("\n      起点： ("+e._s(e.levelMsg.startPosX)+", "+e._s(e.levelMsg.startPosY)+", "+e._s(e.levelMsg.startPosZ)+")\n    ")]),e._v(" "),t("v-timeline-item",[e._v("\n      终点： ("+e._s(e.levelMsg.endPosX)+", "+e._s(e.levelMsg.endPosY)+", "+e._s(e.levelMsg.endPosZ)+")\n    ")]),e._v(" "),t("v-timeline-item",{attrs:{color:"red"}},[t("p",{staticStyle:{margin:"8px"}},[e._v("通关奖励")]),e._v(" "),t("v-collapse",[e.levelMsg.skinMsg?t("v-panel",{attrs:{header:"皮肤奖励",index:"1"}},[t("p",[e._v("皮肤id: "+e._s(e.levelMsg.skinMsg.skinID))]),e._v(" "),t("p",[e._v("皮肤名称: "+e._s(e.levelMsg.skinMsg.skinName))]),e._v(" "),t("p",[e._v("描述: "+e._s(e.levelMsg.skinMsg.description))])]):e._e(),e._v(" "),e.levelMsg.propsMsg?t("v-panel",{attrs:{header:"道具奖励",index:"2"}},[t("p",[e._v("道具id: "+e._s(e.levelMsg.propsMsg.propsID))]),e._v(" "),t("p",[e._v("道具名称: "+e._s(e.levelMsg.propsMsg.propsName))]),e._v(" "),t("p",[e._v("描述: "+e._s(e.levelMsg.propsMsg.description))])]):e._e(),e._v(" "),t("v-panel",{attrs:{header:"金币奖励",index:"3"}},[t("p",[e._v("数量: "+e._s(e.levelMsg.levelGold))])])],1)],1)],1)],1)},staticRenderFns:[]};var a=t("VU/8")(l,v,!1,function(e){t("D5xQ")},"data-v-12a3a9ba",null);s.default=a.exports}});
//# sourceMappingURL=5.45624eec9de379e69bd7.js.map