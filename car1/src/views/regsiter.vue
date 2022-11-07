<template>
  <div class="home">

    <div class="wrapper">
      <div class="name">Car Rental Register</div>
      <div class="cont">
        <img class="img" src="../assets/1.jpg" alt="">
        <el-form  :model="ruleForm" :rules="rules" ref="ruleForm" label-width="140px" class="ruleForm">
        
          <el-form-item label="username" prop="username">
            <el-input placeholder="please write username" v-model="ruleForm.username"></el-input>
          </el-form-item>
          <el-form-item label="password" prop="password">
            <el-input show-password placeholder="please write password" v-model="ruleForm.password"></el-input>
          </el-form-item>
          <el-form-item label="password again" prop="repassword">
            <el-input show-password placeholder="please write password again" v-model="ruleForm.repassword"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button style="width:100% ;" round type="success" @click="submitForm('ruleForm')">register</el-button>
            <!-- <el-button @click="resetForm('ruleForm')">重置</el-button> -->
          </el-form-item>
          <div @click="login" class="register">Login</div>
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
        username: '',
        password: '',
        repassword:""
      },
      rules: {
        username: [
          { required: true, message: 'write username', trigger: 'blur' },
        ],
        password: [
          { required: true, message: 'write password', trigger: 'blur' },
        ],
        repassword: [
          { required: true, message: 'write password again', trigger: 'blur' },
        ]
      }
    };
  },
  methods: {
    login(){
      this.$router.push({ path: '/' });
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
        console.log(this.ruleForm);

       let { username, password,repassword } = this.ruleForm;

        if( password!=repassword){
          this.$message.error('The two passwords are inconsistent, please enter them again');
          return
        }






          // this.axios({
          //       url:"/api/register",
          //       methods:'POST',
          //       data:{
          //          user:username,
          //     pwd:password,
          //     c_pwd:repassword
          //       },
          //       headers:{
          //             'Content-Type':'application/json'
          //       }
          // }).then(res=>{
          //       console.log(res,555555);
          // })

              let  that = this;
          this.axios
            .get(`/api/register?user=${username}&pwd=${password}&c_pwd=${repassword}`, {})

            .then(function (response) {
              console.log(response.data.msg_code);
              if (response.data.msg_code == 200) {
             that.$router.push({ path: '/' });
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
          console.log('error submit!!');
          return false;
        }
      });
    },
  
  }
}
</script>

<style lang="less" scoped>
/deep/ .el-button--success{
  background: #000;
  border: none;
}
  .wrapper {
    padding: 40px 30px 50px;
    min-width: 600px;

    background: #fff;
    border-radius: 5px;
    background: rgba(255, 254, 254, .7);

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
    .ruleForm{
      width: 400px;
      .el-select{
        width: 100%;
      }
    }

  }
  .btns{
    margin: 10px 0  0;
  }
  .register{
    margin: 20px 0 0 120px;
    font-size: 13px;
    text-decoration: underline;
    cursor: pointer;
  }

</style>