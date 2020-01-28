<template>
<div>
  <b-jumbotron id="jbt">
    <template v-slot:header>OpenCV App</template>

    <template v-slot:lead>
      This an assignment website for ECE1779 using Python Flask and OpenCV.
    </template>

    <hr class="my-4">

    <p>
      Written by: Angela, Chad, Feilong.
    </p>

    <b-button class="bbutton" v-if="loggedin" variant="primary" to="/photo">Photo List</b-button>
    <b-button class="bbutton" v-if="!loggedin" variant="success" to="/login">Log In</b-button>
    <b-button class="bbutton" v-if="!loggedin" variant="info" to="/register">Register</b-button>


  </b-jumbotron>
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
.bbutton {
  margin: 0.25rem;
}

#jbt {
  height: 90vh;
  padding-top: 25vh;
}
</style>>
