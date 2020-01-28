<template>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand to="/">OpenCV App</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item v-if="loggedin" to="/photo">Photos</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item v-on:click="testfunc()">TestFunc</b-nav-item>
        <b-nav-item v-if="!loggedin" to="/login">Log In</b-nav-item>
        <b-nav-item  v-if="!loggedin" to="/register">Register</b-nav-item>
        <b-nav-item  v-if="loggedin" to="/about">Sign Out</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>>

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