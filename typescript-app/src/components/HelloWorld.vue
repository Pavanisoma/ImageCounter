<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Image Scoring Application</h1>       
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Image ID</th>
              <th scope="col">Image</th>
              <th scope="col">Score</th>
              <th scope="col">Upvote</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="score in scores" :key="score._id">
              <td>{{ score.imageid }}</td>
              <td><img v-bind:src="'' + score.url" width="100" height="100"/> </td>
              <td>{{ score.count }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button @click="score.count = increment(score.count, score.imageid)">
                  Upvote</button>
                  <button @click="score.count = decrement(score.count, score.imageid)">
                  Downvote</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class HelloWorld extends Vue {
  scores! : any[];
  addImageForm! : any;
  /* eslint-disable */
  data() {
    return {
      scores: [],
      addImageForm: {
        imageid: '',
        url: '',
        count: 0,
      },
    };
  }
    increment(counter, imageid) {
      this.updateScore(imageid, parseInt(counter, 10) + 1);
      return counter + 1;
    }
    decrement(counter, imageid) {
      this.updateScore(imageid, parseInt(counter, 10) - 1);
      return parseInt(counter, 10) - 1;
    }

    // send get request during intialization of app.
    getScore() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.scores = res.data;
          console.log(this.scores);
        })
        .catch((error) => {
          console.error(error);
        });
    }
    updateScore(imageid, count) {
      const payload = {
        imageid,
        count,
      };
      console.log(payload);
      const path = 'http://localhost:5000/';
      axios({
        method: 'put',
        url: path,
        data: payload,
      })
        .then((result) => {
          console.log(result);
        })
        .catch((error) => {
          console.log(error);
        });
    }
    addImage(payload) {
      const path = 'http://localhost:5000/';
      axios({
        method: 'post',
        url: path,
        data: payload,
      })
        .then((result) => {
          console.log(result);
          this.getScore();
        })
        .catch((error) => {
          console.log(error);
          this.getScore();
        });
    }
    initForm() {
      console.log("This is init form");
      this.addImageForm.imageid = '';
      this.addImageForm.url = '';
      this.addImageForm.count = 0;
    }
    onSubmit(evt) {
      evt.preventDefault();
      (this.$refs.addImageModal as Vue & { hide: () => boolean }).hide() 
      const payload = {
        imageid: this.addImageForm.imageid,
        url: this.addImageForm.url,
        count: this.addImageForm.count,
      };
      this.addImage(payload);
      this.initForm();
    }
    onReset(evt) {
      evt.preventDefault();
      (this.$refs.addImageModal as Vue & { hide: () => boolean }).hide()     
      this.initForm();
    }
    created() {
    console.log('ONE TIME ONLY!!');
    this.getScore();
  }
}
</script>




<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
