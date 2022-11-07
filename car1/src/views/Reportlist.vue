<template>
  <div class="home">
    <div class="wrapper">
      <div class="name">
        <i @click="back" class="el-icon-back"></i>
        <div>{{ name }}</div>
        <div></div>
      </div>
      <ul>
        <li
          @click="handle(item.vehNo)"
          :key="index"
          v-for="(item, index) in list"
        >
          {{ item.vehNo}} {{item.vehType}}
          <div class="Electric">
            {{item.vehStatu}}
            <!-- <img style="width: 30px" src="../assets/dc.png" alt="" /> -->
          </div>
        </li>
      </ul>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      type: "",
      list: [],
    };
  },
  mounted() {
    this.name = this.$route.query.name;
    this.type = this.$route.query.type;
    this.getList();
  },
  methods: {
    getList() {
      let that = this;

      this.axios
        .get("/api/showinfo", {})
        .then(function (response) {
           console.log(response.data, 88888);
          that.list = response.data;

         
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    handle(no) {
      let that = this;
      this.axios
        .put(`/api/repair/${no}`, {})
        .then(function (response) {
          that.$message({
            type: "success",
            message: "Repair successful!",
          });
          that.getList();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    // goMy() {
    //   this.$router.push({ path: '/my' });
    // },
    back() {
      this.$router.push({ path: "/operators" });
    },
  },
};
</script>
<style  lang="less" scoped>
ul {
  li {
    box-shadow: 1px 1px 5px #ccc;
    padding: 15px 20px;
    background: #fff;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
}
.btns {
  // width: 400px;
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

    .Electric {
      display: flex;
      align-items: center;
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

.scanner {
  display: block;
  width: 80px;
  margin: 30px auto 0;
  cursor: pointer;
}
</style>