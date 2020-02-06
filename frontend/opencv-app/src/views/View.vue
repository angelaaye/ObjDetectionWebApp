<template>
    <div>
        <el-page-header id="pageheader" @back="$router.go(-1)" content="View Results">
        </el-page-header>

        <EIImageViewer 
                     v-if="showViewer" 
                     :on-close="closeViewer" 
                     :url-list="srcList" />

        <div class="viewbody">
            <div class="viewsingle">
                <el-breadcrumb separator-class="el-icon-arrow-right">
                    <el-breadcrumb-item>View</el-breadcrumb-item>
                    <el-breadcrumb-item>Computed Image</el-breadcrumb-item>
                </el-breadcrumb>

                <el-image 
                    style="max-width: 1280px; max-height: 800px"
                    :src="url" 
                    fit="scale-down">
                </el-image>
            </div>


            <div class="viewsingle">
                <el-breadcrumb separator-class="el-icon-arrow-right">
                    <el-breadcrumb-item>View</el-breadcrumb-item>
                    <el-breadcrumb-item>Original Image</el-breadcrumb-item>
                </el-breadcrumb>

                <el-image 
                    style="max-width: 1280px; max-height: 800px"
                    :src="url" 
                    fit="scale-down">
                </el-image>
            </div>
        </div>
    </div>
</template>>

<script>
import EIImageViewer from 'element-ui/packages/image/src/image-viewer'

export default {
  name: 'imageview',
  components: {
      EIImageViewer
   },
   props: ['id'],
   data() {
      return {
        showViewer: false,
        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        srcList: [
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg'
        ]
      }
    },
    computed: {
        computedSrc: function () {
            return this.srcList;
        }
    }
}
</script>>

<style scoped>
    .viewsingle {
        margin: 22px;
    }

    .viewbody {
        max-width: 1280px;
    }
</style>

