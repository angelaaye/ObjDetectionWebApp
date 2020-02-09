<template>
  <div class="uploaddiv">
    <el-page-header id="pageheader" @back="$router.go(-1)" content="Upload Image">
    </el-page-header>
    <ImageUpload id="imageuploader" />
  </div>
</template>

<script>
// @ is an alias to /src
import ImageUpload from '@/components/ImageUpload.vue'

export default {
  name: 'upload',
  components: {
    ImageUpload
   },
   mounted() {
      var _this = this;
      if (!_this.LOGINSTATUS.hasLoggedIn) {
          _this.$message.error("Unauthorized access, please log in first.");
          _this.$router.push("/login");
          return;
      }
   }
}
</script>

<style scoped>
#pageheader {
  padding: 18px;
}

.uploaddiv {
  padding: 1rem;
  min-width: 35rem;
  margin: auto;
}

#imageuploader {
    margin: 24px
}
</style>