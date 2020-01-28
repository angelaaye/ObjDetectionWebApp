<template>
  <div >
            <h1>Register</h1>
    <b-form id="loginform" @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="User name:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.username"
          type="string"
          required
          placeholder="Enter user name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.password"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-button class="bbutton" type="submit" variant="primary">Register</b-button>
      <b-button class="bbutton" type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.username = ''
        this.form.password = ''
      }
    }
  }
</script>

<style scoped>
h1 {
    margin: 3rem;
}

.bbutton {
    margin: 0.25rem
}

#loginform {
    margin:auto;
    padding: 2rem;
    max-width: 35rem;
}
</style>