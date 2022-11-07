<template>
  <div class="home">
    <div class="wrapper">
      <div class="name">
        <i @click="back" class="el-icon-back"></i>

        <div>Return successFully</div>
        <div></div>
      </div>

      <div class="info">
        <ul>
          <li>
            <div>Vehicle No：</div>
            <div>{{ list.VehNo }}</div>
          </li>
          <li>
            <div>Vehicle Type：</div>
            <div>{{ list.vehType }}</div>
          </li>
          <li>
            <div>Ride time：</div>
            <div>{{ list.Timeused }}</div>
          </li>
          <li>
            <div>Billing：</div>

            <div>＄{{ list.Fee }}</div>
          </li>
        </ul>
        <div @click="pay" class="return">pay</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_id:0,
      list: {
        VehNo: "",
        vehType: "",
        Timeused: "",
        Fee: "",
      },
    };
  },
  mounted() {
    this.list.VehNo = this.$route.query.VehNo;
    this.list.vehType = this.$route.query.vehType;
    this.list.Timeused = this.$route.query.Timeused;
    this.list.Fee = this.$route.query.Fee;
let that = this
    let user = localStorage.getItem("username");
    this.axios
      .post(`/api/showuser/${user}`, {})
      .then(function (response) {
        console.log(response.data);
       that.user_id = response.data[0].user_id; 
      })
      .catch(function (error) {
        console.log(error);
      });

  },
  methods: {
    back() {
      this.$router.push({ path: "/user" });
    },
    pay() {
      let that = this;

      this.axios
        .put(`/api/pay/${this.user_id}/${this.list.VehNo}`, {})
        .then(function (response) {
          console.log(response, 8888);

          that.$message({
            type: "success",
            message: "Payment successful!",
          });

          setTimeout(() => {
            that.$router.push({
              path: "/user",
            });
          }, 2000);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style  lang="less" scoped>
.info {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 400px;
  // border: 1px solid #000;
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
.btns {
  width: 400px;
  margin: 30px auto 0;
  display: flex;
  align-items: center;
  justify-content: space-between;

  /deep/ .el-button--success {
    background: #000;
    border: none;
    width: 100%;
    height: 45px;
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

.scanner {
  widows: 80px;
  margin: 10px auto 0;
  cursor: pointer;
}
</style>