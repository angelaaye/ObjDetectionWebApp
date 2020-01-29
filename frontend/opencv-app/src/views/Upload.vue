<template>
  <div class="uploaddiv">
    <el-page-header id="pageheader" @back="$router.go(-1)" content="Upload Image">
    </el-page-header>
    <ImageUpload id="imageuploader" />
        <p> Click "+" to choose an image.</p>
  </div>
</template>

<script>
// @ is an alias to /src
import ImageUpload from '@/components/ImageUpload.vue'

export default {
  name: 'upload',
  components: {
    ImageUpload
   }
}
</script>

<style scoped>
#pageheader {
  padding: 18px;
}

.uploaddiv {
  padding: 1rem;
  max-width: 35rem;
  margin: auto;
}

#imageuploader {
    margin: 24px
}
</style>