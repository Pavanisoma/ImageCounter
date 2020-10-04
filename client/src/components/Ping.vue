<template>
  <div class="hello">
    <!-- <table class="table table-hover">
          <tbody>
            <tr v-for="(book, index) in scores" :key="index">
              <td>{{ book.score1 }}</td>
              <td>{{ book.score2 }}</td>
            </tr>
          </tbody>
    </table> -->
    <ul>
    <li><img alt="Vue logo" src="../assets/logo.png" width="50" height="50"></li>
    <li><p>Score</p></li>
    <li><p>{{ptr1}}</p></li>
    <li><button @click="ptr1 = increment(ptr1)">+1</button></li>
    <li><button @click="ptr1 = decrement(ptr1)">-1</button></li>
    </ul>
    <ul>
    <li><img alt="Vue logo" src="../assets/logo.png"  width="50" height="50"></li>
    <li><p>Score</p></li>
    <li><p>{{ptr2}}</p></li>
    <li><button @click="ptr2 = increment(ptr2)">+1</button></li>
    <li><button @click="ptr2 = decrement(ptr2)">-1</button></li>
    </ul>
    <ul>
    <li><img alt="Vue logo" src="../assets/logo.png"  width="50" height="50"></li>
    <li><p>Score</p></li>
    <li><p>{{ptr3}}</p></li>
    <li><button @click="ptr3 = increment(ptr3)">+1</button></li>
    <li><button @click="ptr3 = decrement(ptr3)">-1</button></li>
    </ul>
    <ul>
    <li><img alt="Vue logo" src="../assets/logo.png"  width="50" height="50"></li>
    <li><p>Score</p></li>
    <li><p>{{ptr4}}</p></li>
    <li><button @click="ptr4 = increment(ptr4)">+1</button></li>
    <li><button @click="ptr4 = decrement(ptr4)">-1</button></li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      scores: [],
      ptr1: 0,
      ptr2: 0,
      ptr3: 0,
      ptr4: 0,
    };
  },
  methods: {
    increment(counter) {
      return counter + 1;
    },
    decrement(counter) {
      return counter - 1;
    },
    // send get request during intialization of app.
    getScore() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.ptr1 = parseInt(res.data.score1, 10);
          this.ptr2 = parseInt(res.data.score2, 10);
          this.ptr3 = parseInt(res.data.score3, 10);
          this.ptr4 = parseInt(res.data.score4, 10);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    addscore() {
      const payload = {
        score1: this.ptr1,
        score2: this.ptr2,
        score3: this.ptr3,
        score4: this.ptr4,
      };
      console.log(payload);
      const path = 'http://localhost:5000/';
      axios({
        method: 'post',
        url: path,
        data: payload,
      })
        .then((result) => {
          console.log(result);
          this.ptr1 = parseInt(result.data.score1, 10);
          this.ptr2 = parseInt(result.data.score2, 10);
          this.ptr3 = parseInt(result.data.score3, 10);
          this.ptr4 = parseInt(result.data.score4, 10);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    console.log('ONE TIME ONLY!!');
    this.getScore();
  },
  updated() {
    console.log('for every click');
    this.addscore();
  },
};
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
