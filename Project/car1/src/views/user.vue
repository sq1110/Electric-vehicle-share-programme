<template>
  <div class="home">
    <div class="wrapper">
      <div class="name">
        <i @click="goMy" class="el-icon-s-custom"></i>
        <div>Car Rental</div>

        <div @click="out" class="out">
          <img src="../assets/out.png" alt="" />
        </div>
      </div>
      <div class="map">
        <img src="../assets/map.png" alt="" />
      </div>

      <div class="inline" v-if="flag">
        <div></div>
        <img @click="open" class="scanner" src="../assets/scaner.png" alt="" />

        <img @click="check" class="check" src="../assets/check.png" alt="" />
      </div>

      <div v-else class="info">
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
            <div>0 min</div>
          </li>
          <li>
            <div>Billing：</div>

            <div>＄ 2.00</div>
          </li>
        </ul>
        <div @click="Return" class="return">Return</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      flag: true,
      list: [],
      No: "",
    };
  },
  methods: {
    Return() {
      let that = this;
      this.$prompt("Please enter return location", "Tips", {
        confirmButtonText: "confirm",
        cancelButtonText: "cancel",
      })
        .then(({ value }) => {
          if (!value) {
            this.$message({
              type: "info",
              message: "Please enter return location",
            });

            return;
          }

          that.axios
            .put(`/api/return/${that.No}/${value}`, {})
            .then(function (response) {
              console.log(response, 8888);

              let { VehNo, vehType, Timeused, Fee } = that.list;

              that.$router.push({
                path: "/pay",
                query: {
                  VehNo,
                  vehType,
                  Timeused,
                  Fee,
                },
              });
            })
            .catch(function (error) {
              console.log(error);
            });
        })

        .catch(() => {
          this.flag = true;
          this.$message({
            type: "info",
            message: "Cancel operation",
          });
        });
    },
    check() {
      
      let that = this;
      this.$prompt("Please enter vehno: ", "Tips", {
        confirmButtonText: "confirm",
        cancelButtonText: "cancel",
      })
        .then(({ value }) => {
          that.No = value;
          this.axios
            .put(`/api/report/${value}`, {})
            .then(function (response) {
              that.$message({
            type: "success",
            message: "Report successful!",
          });
            })
            .catch(function (error) {
              console.log(error);
            });
        })
        .catch(() => {
          this.flag = true;
          this.$message({
            type: "info",
            message: "Cancel operation",
          });
        });
    
    },

    out() {
      this.$router.push({ path: "/" });
    },

    // /return/<int:no>/<string:loc>
    goMy() {
      this.$router.push({ path: "/my" });
    },

    open() {
      let that = this;
      this.$prompt("Please enter vehno", "Tips", {
        confirmButtonText: "confirm",
        cancelButtonText: "cancel",
        // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        // inputErrorMessage: '邮箱格式不正确'
      })
        .then(({ value }) => {
          that.No = value;
          this.axios
            .put(`/api/rent/${value}`, {})
            .then(function (response) {
              that.axios
                .post("/api/searchv", {})
                .then(function (response) {
                  console.log(response.data, 88888888);
                  let resDate = response.data.filter((s) => s.VehNo == that.No);

                  that.list = resDate[0];
                  // response.data[0];
                  that.flag = false;
                })
                .catch(function (error) {
                  console.log(error);
                });
            })
            .catch(function (error) {
              console.log(error);
            });

          // this.flag = false
          // this.$message({
          //   type: 'success',
          //   message: '你的邮箱是: ' + value
          // });
        })
        .catch(() => {
          this.flag = true;
          this.$message({
            type: "info",
            message: "Cancel operation",
          });
        });
    },

    // open() {
    //     this.$confirm('确认借车吗？', 'warnniing', {
    //       confirmButtonText: 'sure',
    //       cancelButtonText: 'cancel',
    //       type: 'warning'
    //     }).then(() => {
    //       this.flag = false
    //       this.$message({
    //         type: 'success',
    //         message: 'sure!'
    //       });
    //     }).catch(() => {
    //       this.flag = true
    //       this.$message({
    //         type: 'info',
    //         message: 'cancel'
    //       });
    //     });
    //   }
  },
};
</script>
<style  lang="less" scoped>
.inline {
 margin: 30px auto 0;
  width: 400px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  .check {
    width: 40px;
  }
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
 
  cursor: pointer;
}
</style>