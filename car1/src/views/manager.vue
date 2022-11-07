<template>
  <div class="home">
    <div class="wrapper">
      <div class="name">
        <!-- <i @click="goMy" class="el-icon-s-custom"></i> -->
        <div>Car Rental</div>

        <div @click="out" class="out">
          <img src="../assets/out.png" alt="" />
        </div>
      </div>
      <div class="map">
        <img src="../assets/map.png" alt="" />
      </div>

      <el-button
        @click="go"
        style="width: 400px; font-size: 18px; margin: 20px 0; height: 45px"
        round
        type="success"
        >Detail</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      flag: true,
    };
  },
  methods: {
    out() {
      this.$router.push({ path: "/" });
    },
    goMy() {
      this.$router.push({ path: "/my" });
    },
    go() {
      window.location.href = "http://127.0.0.1:8080/";
      // this.axios
      // .get("/api/location")

    },
    
  },
};
</script>
<style  lang="less" scoped>
/deep/ .el-button--success {
  background: #000;
  border: none;
}
.info {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 400px;
  border: 1px solid #000;
  border-radius: 5px;
  margin: 30px auto 0;
}
.return {
  width: 90px;
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0px 0px 10px #6d6c6c;
  margin-right: 20px;
  font-weight: bold;
  font-size: 20px;
  cursor: pointer;
  background: #fff;
}
ul {
  flex: 1;

  list-style: none;
  padding-top: 30px;
  li {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    > div:nth-child(1) {
      width: 110px;
      text-align: left;
      margin-left: 20px;
    }
    > div:nth-child(2) {
      flex: 1;
      text-align: left;
      font-weight: bold;
    }
  }
}
.wrapper {
  padding: 40px 30px 50px;
  min-width: 480px;
  background: #fff;
  border-radius: 5px;
  background: rgba(255, 254, 254, 0.7);
}

.name {
  font-size: 30px;
  text-align: center;
  font-weight: bold;
  padding: 0 0 40px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.my {
  width: 50px;
  cursor: pointer;
}

.map {
  width: 400px;

  margin: 0 auto;
  border-radius: 5px;
}

.scanner {
  display: block;
  width: 80px;
  margin: 30px auto 0;
  cursor: pointer;
}
</style>