<template>
<el-menu 
  :default-active="$route.path"
  class="el-menu-demo"
  mode="horizontal"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#fff" router>
  <el-row>
    <el-col :xs={span:18} :sm={span:18} :md={span:4} :lg={span:2}>
      <el-row type="flex">
        <el-menu-item index="/">スマ写真  Home</el-menu-item>
      </el-row>
    </el-col>

    <el-col :xs={span:6} :sm={span:6} :md={span:20} :lg={span:22}>
      <el-row class="hidden-md-and-up">
        <el-submenu index="/">
          <template slot="title"><i class="el-icon-menu"></i></template>
          <el-menu-item v-if="loggedin" index="/upload">Upload</el-menu-item>
          <el-menu-item v-if="loggedin" index="/result">Results</el-menu-item>
          <el-menu-item v-if="!loggedin" index="/login">Log In</el-menu-item>
          <el-menu-item v-if="!loggedin" index="/register">Register</el-menu-item>
          <el-menu-item v-if="loggedin" @click="onSignOut()">Sign Out</el-menu-item>
        </el-submenu>
      </el-row>
      <el-row class='hidden-sm-and-down' type="flex" justify="space-between">
        <el-col :span=8>
          <el-row type="flex">
             <el-menu-item v-if="loggedin" index="/upload">Upload</el-menu-item>
             <el-menu-item v-if="loggedin" index="/result">Results</el-menu-item>
          </el-row>
        </el-col>

        <el-col :md={span:5} :lg={span:3}>
          <el-row type="flex" justify="space-between">
            <el-menu-item v-if="!loggedin" index="/login">Log In</el-menu-item>
            <el-menu-item v-if="!loggedin" index="/register">Register</el-menu-item>
            <el-menu-item v-if="loggedin" @click="onSignOut()">Sign Out</el-menu-item>
          </el-row>
        </el-col>
        
      </el-row>
    </el-col>
</el-row>
</el-menu>
</template>


<script>
import axios from "axios";

export default {
  name: 'NavBar',
  data: function () {
    return {
      loginStatus: this.LOGINSTATUS
    }
  },
  mounted() {
    // After mounted, check if cookie exists and restore login status.
    if (this.$cookie.get('csrf_access_token')) {
      this.LOGINSTATUS.hasLoggedIn = true;
    }
  },
  computed: {
    loggedin: function () {return this.loginStatus.hasLoggedIn}
  },
  methods: {
    testfunc: function () {
      this.LOGINSTATUS.hasLoggedIn = !this.LOGINSTATUS.hasLoggedIn;      
    },

    onSignOut: function () {
      let _this = this;
      axios({
              method: 'GET',
              url: "/api/user/logout",
              withCredentials: true
            })
            .then((response) => {
              if (response.status == 200) {
                this.$message.success("Log out successfully.");
                this.LOGINSTATUS.hasLoggedIn = false;
                if (_this.$router.currentRoute.path !== '/') {
                  _this.$router.push('/');
                }
              }
            })
            .catch((error) => {
              this.$message.error("Error: code " + error.response.status);
            })
    }
  }
}
</script>

<style>

</style>