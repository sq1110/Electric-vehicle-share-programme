<template>
  <div id="app">
    <!-- <router-view name="Header" style="background-color: white"></router-view> -->

    <div class="public-width width-auto">
      <div class="bg"></div>
      <!-- <KeepAlive> -->
        <router-view> </router-view>
      <!-- </KeepAlive> -->
      
    </div>

    <!-- <router-view name="Bottom"></router-view> -->
  </div>
</template>

<script>
// import { Header } from "@/components/Header.vue";
// export default {
//   components() {
//     // Header;
//   },
// };
</script>

<style lang="less">
.map img{
  width: 100%;
}
// 全局样式文件
* {
  padding: 0;
  margin: 0;
}

.flex {
  display: flex;
  justify-items: self-end;
  // justify-items: s;
}

.wrap {
  flex-wrap: wrap;
}

.p-r {
  position: relative;
}

.p-a {
  position: absolute;
}

.jus-sb {
  justify-content: space-between; 
}

.jus-sa {
  justify-content: space-around; 
}

.jus-c {
  justify-items: center;
}

.item-cen {
  align-items: center;
}

.item-st {
  align-items: flex-start;

}

.item-en {
  align-items: flex-end;
}

@b_c_1: rgba(255, 255, 255, 0.493);

a {
  text-decoration: none;
}

.home {
  display: flex;
  align-items: center;
  justify-content: center;
  ;
  width: 100%;
  height: 100vh;

}

.bg {
  position: absolute;
  z-index: -1;
  filter:blur(5px);
  width: 100%;
  height: 100vh;
  background: url('./assets/bg.jpg') center / cover no-repeat;
}

.width-auto {
  margin: 0 auto;
}

.p-r {
  position: relative;
}

.position-abs-100 {
  position: absolute;
  width: 100%;
  left: 0;
}

// 主页标题marg距离
.index-h2 {
  // margin: 60px 0;
  padding-top: 120px;
  padding-bottom: 60px;
  text-align: center;
}

// 布局背景色
.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

// 盒子阴影
.box-sh-i {
  box-shadow: inset 1px 5px 15px #bfbfbf98;
}

.box-sh {
  box-shadow: 1px 5px 15px #bfbfbf73;
}

.el-col {
  // border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.el-image__error {
  border: red 1px solid;
}

.bj1 {
  background: #e5e9f2;
}

.bj2 {
  background: #d3dce6;
}

.bj3 {
  background: #c6ced8;
}

.bj4 {
  background: #b2b9c2;
}

body {
  height: 100%;
  background: #f7f7f7;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.out{
  img{
    cursor: pointer;
    width: 35px;
  }
}
</style>
