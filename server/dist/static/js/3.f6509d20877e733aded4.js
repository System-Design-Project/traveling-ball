webpackJsonp([3],{i2RG:function(t,e){},lO7g:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n={render:function(){var t=this.$createElement,e=this._self._c||t;return e("v-card",{attrs:{id:"home-welcome-page"}},[e("v-layout",[e("v-sider",{staticClass:"home-left-nav",staticStyle:{background:"#aaa",padding:"20px 0"},attrs:{width:260}},[e("v-tabs",{attrs:{"active-tab-key":"/user"},on:{change:this.onChange}},[e("v-tab-pane",{staticStyle:{"font-size":"20px"},attrs:{"tab-key":"/user",tab:"用户"}},[e("v-menu",{staticStyle:{background:"#aaa"},attrs:{mode:"inline",data:this.userPages},on:{"item-click":this.onClick}})],1),this._v(" "),e("v-tab-pane",{attrs:{"tab-key":"/manage",tab:"管理"}},[e("v-menu",{staticStyle:{background:"#aaa"},attrs:{mode:"inline",data:this.mngPages},on:{"item-click":this.onClick}})],1)],1)],1),this._v(" "),e("v-content",{style:{padding:"24px"}},[e("router-view")],1)],1)],1)},staticRenderFns:[]};var s=a("VU/8")({data:function(){return{userPages:[{name:"道具",selected:!0},{name:"皮肤"},{name:"关卡"}],mngPages:[{name:"道具",selected:!0},{name:"皮肤"},{name:"关卡"},{name:"游戏版本"}],toRoute:{"道具":"/props","皮肤":"/skins","关卡":"/levels","游戏版本":"/versions"},urlType:"/user"}},created:function(){this.$router.push({path:"/user/props"})},methods:{onChange:function(t){this.urlType=t},onClick:function(t){this.$router.push({path:this.urlType+this.toRoute[t[0].name]})}}},n,!1,function(t){a("i2RG")},"data-v-1c475e92",null);e.default=s.exports}});
//# sourceMappingURL=3.f6509d20877e733aded4.js.map