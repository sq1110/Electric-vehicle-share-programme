<template>
  <div class="home">
    <div class="wrapper">
      <div class="name">Car Rental</div>
      <div class="cont">
        <img class="img" src="../assets/1.jpg" alt="" />
        <el-form
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="100px"
          class="ruleForm"
        >
          <el-form-item label="role" prop="role">
            <el-select v-model="ruleForm.role" placeholder="please choice role">
              <el-option label="manager" value="manager"></el-option>
              <el-option label="operators" value="operators"></el-option>
              <el-option label="user" value="user"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="username" prop="username">
            <el-input
              placeholder="please enter username"
              v-model="ruleForm.username"
            ></el-input>
          </el-form-item>
          <el-form-item label="password" prop="password">
            <el-input
              show-password
              placeholder="please enter password"
              v-model="ruleForm.password"
            ></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button
              style="width: 100%"
              round
              type="success"
              @click="submitForm('ruleForm')"
              >login</el-button
            >
            <!-- <el-button @click="resetForm('ruleForm')">重置</el-button> -->
          </el-form-item>
          <div @click="regsiter" class="register">No account? Register...</div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ruleForm: {
        role: "",
        username: "",
        password: "",
      },
      rules: {
        username: [
          { required: true, message: "write username", trigger: "blur" },
        ],
        password: [
          { required: true, message: "write password", trigger: "blur" },
        ],
        role: [{ required: true, message: "choice role", trigger: "change" }],
      },
    };
  },

  methods: {
    regsiter() {
      this.$router.push({ path: "/regsiter" });
    },
    submitForm(formName) {
      let that = this;
      this.$refs[formName].validate((valid) => {
        if (valid) {

          let { username, password } = this.ruleForm;

          this.axios
            .get(`/api/login?user=${username}&pwd=${password}`, {})

            .then(function (response) {
              console.log(response.data.msg_code);
              if (response.data.msg_code == 200) {

                localStorage.setItem('username',username)
                console.log(that.ruleForm.role, 5555555555);
                if (that.ruleForm.role == "manager") {
                  that.$router.push({ path: "/manager" });
                } else if (that.ruleForm.role == "operators") {
                  that.$router.push({ path: "/operators" });
                } else {
                  that.$router.push({ path: "/user" });
                }
              } else {
                that.$message({
                  type: "success",
                  message: "Please enter correct username and password!",
                });
              }
            })
            .catch(function (error) {
              console.log(error);
            });

          // return
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
  },
};
</script>

<style lang="less" scoped>
/deep/ .el-button--success {
  background: #000;
  border: none;
}
.wrapper {
  padding: 40px 30px 50px;
  min-width: 600px;

  background: #fff;
  border-radius: 5px;
  background: rgba(255, 254, 254, 0.7);
}

.name {
  font-size: 30px;
  text-align: center;
  font-weight: bold;
  padding: 0 0 40px 0;
}

.cont {
  display: flex;
  // align-items: center;
  justify-content: space-between;

  .img {
    width: 300px;
  }
  .ruleForm {
    width: 400px;
    .el-select {
      width: 100%;
    }
  }
}
.btns {
  margin: 10px 0 0;
}
.register {
  margin: 20px 0 0 120px;
  font-size: 13px;
  text-decoration: underline;
  cursor: pointer;
}
</style>