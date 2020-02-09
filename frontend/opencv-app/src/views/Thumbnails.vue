<template>
<div id="waterfall-wrapper">
    <el-page-header id="pageheader" @back="$router.go(-1)" content="View Results">
    </el-page-header>
    <el-row v-loading="isLoading">
    <p align="left">Click on the thumbnail to view the results.</p>
    <div class="waterfalls">
        <EIImageViewer ref="imgviewer"
                v-if="showViewer" 
                :on-close="closeViewer" 
                :url-list="compViewerSrc()" />
        <div class="box" v-for="imgsrc in srcList" v-bind:key="imgsrc">
            <div class="pic"><img :src="compThumbSrc(imgsrc)" :alt="imgsrc" @click="onPreview(imgsrc)"></div>
        </div>
    </div>
    </el-row>

</div>
</template>

<style scoped>
#pageheader {
    margin: 20px 10px;
}

#waterfall-wrapper {
   margin: 0 auto;
   max-width: 85vw;
}    
.waterfalls {
    padding:10px;
    position: relative;
    margin: 0 auto;
    columns:200px;
    column-gap: 20px; 
}    
.box {
    break-inside: avoid;   
    margin-bottom:15px;    
    color:white;      
    border-radius:5px;    
}
.pic img {
    width: 100%;
    height: 100%;
    border-radius: 5px;  
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

</style>

<script>
import EIImageViewer from 'element-ui/packages/image/src/image-viewer'
import axios from 'axios';

export default {
  name: 'thumbnaillist',
  components: {
      EIImageViewer
   },
   props: [],
   mounted() {
        var _this = this;
        if (!_this.LOGINSTATUS.hasLoggedIn) {
            _this.$message.error("Unauthorized access, please log in first.");
            _this.$router.push("/login");
            return;
        }

        axios({
                method: 'GET',
                url: "/api/photo/",
                withCredentials: true
            })
            .then((response) => {
                if (response.status == 200) {
                    let id_list = response.data.map(photo => { return photo.id; })
                    id_list.map(id => { _this.srcList.unshift(id) });
                    _this.isLoading = false;
                }
            })
            .catch((error) => {
                this.$message.error("Loading image list failed, error code: " + error.status);
                window.console.log(error);
            })
   },
   data() {
      return {
        isLoading: true,
        showViewer: false,
        srcList: [],
        viewerID: -1
      }
    },
    methods: {
        onPreview(id) {
          this.showViewer = true;
          this.viewerID = id;
          this.$message.info("Use buttons on the sides to toggle between processed and original images.");
        },
        genSrcLink(type, id) {
            return 'http://localhost:5000/api/photo/' + type + '/' + id;
        },
        closeViewer() {
          this.showViewer = false;
          this.viewerID = -1;
        },
        compThumbSrc(id) {
            return this.genSrcLink('thumbnail', id);
        },
        compViewerSrc() {
            return [
                this.genSrcLink('processed', this.viewerID),
                this.genSrcLink('original', this.viewerID)
            ]
        }

    }
}
</script>>