<template>
  <div class="home">
    <div class="wrapper">
      <div class="name">
        <i @click="back" class="el-icon-back"></i>

        <div>Car Rental</div>
        <div></div>
      </div>
      <img class="scanner" src="../assets/photo.png" alt="" />
      <ul>
        <li>
          <div>Name：</div>
          <div>{{ info.name }}</div>
        </li>
        <li>
          <div>Gender：</div>
          <div>Male</div>
        </li>
        <li>
          <div>Total riding time：</div>
          <div>2h</div>
        </li>
        <li>
          <div>Balance：</div>
          <div>£ {{ info.balance }}</div>
        </li>
      </ul>
      <div class="btns">
        <el-button @click="recharge" round type="success">Recharge</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      info: {
        name:'',
        balance:''
      },
    };
  },

  mounted() {
   this.getlist()
  },
  methods: {


    getlist(){

       let that = this;
    let user = localStorage.getItem("username");
    this.axios
      .post(`/api/showuser/${user}`, {})
      .then(function (response) {
        console.log(response.data);
       that.info.name = response.data[0].user_name; 
       that.info.balance= response.data[0].user_balance;
      })
      .catch(function (error) {
        console.log(error);
      });

    },
    recharge(){

       let that = this;
    let user = localStorage.getItem("username");
    this.axios
      .put(`/api/recharge/${user}`, {})
      .then(function (response) {
         that.$message({
            type: "success",
            message: "Recharge successful!",
          });
          that.getlist()
      })
      .catch(function (error) {
        console.log(error);
      });


      
    },
    back() {
      this.$router.push({ path: "/user" });
    },
  },
};
</script>
<style  lang="less" scoped>
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
ul {
  margin: 20px 0 0 90px;
  list-style: none;
  li {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    > div:nth-child(1) {
      width: 150px;
      text-align: right;
      margin-right: 10px;
    }
    > div:nth-child(2) {
      flex: 1;
      text-align: left;
      font-weight: bold;
    }
  }
}
</style>