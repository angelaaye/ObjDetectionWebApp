<template>
<div id="welcomediv">
    <h1>ECE1779 Assignment 1</h1>

    <br>

    <p>
      This an assignment website for ECE1779 using Python Flask and OpenCV.
    </p>

    <hr>

    <p>
      Written by: Angela, Chad, Feilong.
    </p>
    <br>

    <el-button type="primary" v-if="loggedin" @click="$router.push('upload')">Upload</el-button>
    <el-button v-if="loggedin" @click="$router.push('result')">Results</el-button>
    <el-button type="primary" v-if="!loggedin" @click="$router.push('login')">Log In</el-button>
    <el-button v-if="!loggedin" @click="$router.push('register')">Register</el-button>

</div>
</template>

<script>

export default {
  name: 'Welcome',
  data: function () {
    return {
      loginStatus: this.LOGINSTATUS
    }
  },
  computed: {
    loggedin: function () {return this.loginStatus.hasLoggedIn}
  }
}
</script>

<style scoped>
#welcomediv {
  max-width: 1000px;
  margin: auto;
  padding: 28px;
}
</style>>
