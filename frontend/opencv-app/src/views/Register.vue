<template>
<div class="logindiv">
  <el-page-header id="pageheader" @back="$router.go(-1)" content="Register">
  </el-page-header>
  <hr>
<el-form :model="loginform" status-icon :rules="rules" ref="loginform" label-width="100px" class="loginform">
  <el-form-item label="Username" prop="username">
    <el-input type="text" v-model="loginform.username" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="Password" prop="password">
    <el-input type="password" v-model="loginform.password" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('loginform')">Register</el-button>
    <el-button @click="resetForm('loginform')">Reset</el-button>
  </el-form-item>
</el-form>
</div>
</template>
<script>
  import axios from 'axios';

  export default {
    data() {
       var validateName = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter unsername.'));
        } else {
          callback();
        }
      };
       var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter password.'));
        } else {
          callback();
        }
      };
      return {
        loginform: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            { validator: validateName, trigger: 'blur' }
          ],
          password: [
            { validator: validatePass, trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // Valid front-end data
            let formData = new FormData();
            formData.set('id', -1);
            formData.set('username', this.loginform.username);
            formData.set('password', this.loginform.password);

            axios({
              method: 'POST',
              url: "http://localhost:5000/api/user/register",
              data: formData,
              headers: {'Content-Type': 'multipart/form-data'}
            })
            .then((response) => {
              if (response.status == 200) {
                this.$message.success("Register success!");
              }
              window.console.log(response);
            })
            .catch((error) => {
              this.$message.error("Error: " + error.status);
              window.console.log(error);
            })
          } else {
            this.$message.success("Error! Please validate your input!");
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style scoped>
#pageheader {
  padding: 18px;
}

.loginform {
  margin: auto;
  padding-right: 18px;
}

.logindiv {
  padding: 1rem;
  max-width: 35rem;
  margin: auto;
}
</style>