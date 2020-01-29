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
        <el-menu-item index="/">OpenCV App Home</el-menu-item>
      </el-row>
    </el-col>

    <el-col :xs={span:6} :sm={span:6} :md={span:20} :lg={span:22}>
      <el-row class="hidden-md-and-up">
        <el-submenu>
          <template slot="title"><i class="el-icon-menu"></i></template>
          <el-menu-item v-if="!loggedin" index="/">Upload</el-menu-item>
          <el-menu-item v-if="!loggedin" index="/">Results</el-menu-item>
          <el-menu-item @click="testfunc()">FrontEndTestLogin</el-menu-item>
          <el-menu-item v-if="!loggedin" index="/login">Log In</el-menu-item>
          <el-menu-item v-if="!loggedin" index="/register">Register</el-menu-item>
          <el-menu-item v-if="loggedin" index="/about">Sign Out</el-menu-item>
        </el-submenu>
      </el-row>
      <el-row class='hidden-sm-and-down' type="flex" justify="space-between">
        <el-col :span=8>
          <el-row type="flex">
             <el-menu-item v-if="!loggedin" index="/">Upload</el-menu-item>
             <el-menu-item v-if="!loggedin" index="/">Results</el-menu-item>
          </el-row>
        </el-col>

        <el-col :span=8>
          <el-row type="flex" justify="space-between">
            <el-menu-item @click="testfunc()">FrontEndTestLogin</el-menu-item>
            <el-menu-item index="/about">TestPage</el-menu-item>
            <el-menu-item v-if="!loggedin" index="/login">Log In</el-menu-item>
            <el-menu-item v-if="!loggedin" index="/register">Register</el-menu-item>
            <el-menu-item v-if="loggedin" index="/about">Sign Out</el-menu-item>
          </el-row>
        </el-col>
        
      </el-row>
    </el-col>
    <!-- 
    <el-col sm=6>
      <span>
        <el-menu-item v-if="loggedin" index="/">Upload</el-menu-item>
        <el-menu-item v-if="loggedin" index="/">Results</el-menu-item>
      </span>
      <el-row>
        <el-menu-item @click="testfunc()">FrontEndTestLogin</el-menu-item>
        <el-menu-item index="/about">TestPage</el-menu-item>
        <el-menu-item v-if="!loggedin" index="/login">Log In</el-menu-item>
        <el-menu-item v-if="!loggedin" index="/register">Register</el-menu-item>
        <el-menu-item v-if="loggedin" index="/about">Sign Out</el-menu-item>
      </el-row>
    </el-col> -->
</el-row>
</el-menu>
</template>


<script>
export default {
  name: 'NavBar',
  data: function () {
    return {
      loginStatus: this.LOGINSTATUS
    }
  },
  computed: {
    loggedin: function () {return this.loginStatus.hasLoggedIn}
  },
  methods: {
    testfunc: function () {
      this.LOGINSTATUS.hasLoggedIn = !this.LOGINSTATUS.hasLoggedIn;      
    }
  }
}
</script>

<style>

</style>