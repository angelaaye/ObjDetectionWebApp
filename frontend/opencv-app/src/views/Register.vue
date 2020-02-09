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
          callback(new Error('Please enter username.'));
        } else if (value.length > 20) {
          callback(new Error('Username longer than 20 characters.'));
        } else {
          callback();
        }
      };
       var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter password.'));
        } else if (value.length > 20) {
          callback(new Error('Password too long, restrict to between 4 and 20 characters or less.'));
        } else if (value.length < 4) {
          callback(new Error('Password too weak, restrict to between 4 and 20 characters or less.'));
        }
        else {
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
        let _this = this;
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // Valid front-end data
            let formData = new FormData();
            formData.set('id', -1);
            formData.set('username', this.loginform.username);
            formData.set('password', this.loginform.password);

            axios({
              method: 'POST',
              url: "/api/user/register",
              data: formData,
              headers: {'Content-Type': 'multipart/form-data'}
            })
            .then((response) => {
              if (response.status == 200) {
                this.$message.success("Register success! You can login now.");
                setTimeout(function() {
                  _this.$router.push('/login');
                }, 1000);
              }
              window.console.log(response);
            })
            .catch((error) => {
              if (error.response.status == 401) {
                this.$message.error("Error: Username already taken!");
              }
              
              window.console.log(error);
            })
          } else {
            this.$message.error("Error! Please validate your input!");
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