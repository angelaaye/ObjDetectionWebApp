<template>
<div id="waterfall-wrapper">
    <el-page-header id="pageheader" @back="$router.go(-1)" content="View Results">
    </el-page-header>
    <div class="waterfalls">
        <EIImageViewer 
                v-if="showViewer" 
                :on-close="closeViewer" 
                :url-list="srcList" />
        <div class="box" v-for="imgsrc in srcList" v-bind:key="imgsrc">
            <div class="pic"><img :src="compThumbSrc(imgsrc)" :alt="imgsrc" @click="onPreview(imgsrc)"></div>
        </div>
    </div>
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

export default {
  name: 'thumbnaillist',
  components: {
      EIImageViewer
   },
   props: [],
   data() {
      return {
        showViewer: false,
        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        srcList: [
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
        ],
        viewerID: -1
      }
    },
    computed: {
        viewerSrc: function () {
            return [
                'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
            ]
        }
    },
    methods: {
        onPreview(id) {
          this.showViewer = true;
          this.viewerID = id;
        },
        closeViewer() {
          this.showViewer = false;
          this.viewerID = -1;
        },
        compThumbSrc(id) {
            return id;
        },
        compViewerSrc(id) {
            id;
            return [
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg'
            ]
        }
    }
}
</script>>