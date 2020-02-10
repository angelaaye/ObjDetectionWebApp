<template>
<div>
    <el-upload
    v-loading="isUploading"
    class="avatar-uploader"
    action="/api/photo/"
    name="photo"
    with-credentials
    :headers="{'X-CSRF-TOKEN': csrf_access_token}"
    :show-file-list="false"
    :on-progress="handleProgress"
    :on-success="handleAvatarSuccess"
    :on-error="handleAvatarError"
    :before-upload="beforeAvatarUpload">
    <img v-if="imageUrl" :src="imageUrl" class="avatar">
    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
    <p v-if="!this.imageUrl">Click "+" to upload an image.</p>
    <p v-if="this.imageUrl">Click the above area to upload another image.</p>

</div>
</template>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    min-width: 178px;
    min-height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    min-width: 178px;
    min-height: 178px;
    max-width: 90vw;
    max-height: 90vh;
    display: block;
  }
</style>

<script>
  export default {
    data() {
      return {
        imageUrl: '',
        isUploading: false,
        csrf_access_token: this.$cookie.get('csrf_access_token')
      };
    },
    methods: {
      onReset() {
          this.imageUrl = '';
      },
      handleAvatarSuccess(res, file) {
        this.isUploading = false;
        this.imageUrl = URL.createObjectURL(file.raw);
        this.$message.success('Picture uploaded and processed successfully!');
      },
      handleAvatarError(err) {
        this.$message.error("Error" + err.response.status);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isPNG = file.type === 'image/png';

        const isLt2M = file.size / 1024 / 1024 < 10;

        if (!isJPG && !isPNG) {
          this.$message.error('Can only upload jpg or png files!');
        }
        if (!isLt2M) {
          this.$message.error('Cannot upload image more than 10 MB!');
        }

        return (isJPG || isPNG) && isLt2M;
      },
      handleProgress() {
        this.isUploading = true;
      }
    }
  }
</script>