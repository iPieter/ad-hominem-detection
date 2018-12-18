<template>
  <div id="app" class="container">
    <div class="row mt-2">
      <h1 class="pl-0 col-md-6 offset-md-3">Go on, insult us ...</h1>
    </div>

    <div class="form-group row">
      <textarea class="col-md-6 offset-md-3 form-control" v-model="current" rows="3"></textarea>
    </div>
    <div class="row">
      <button class="btn btn-primary col-md-6 offset-md-3" v-on:click="call()">Submit form</button>
    </div>

    <ul class="list-group row mt-4">
      <li v-for="query in oldQueries" class="list-group-item col-md-6 offset-md-3">
        <div class="row">
          <div class="col-md-3">
            <span v-if="query.result < 0.78" class="badge badge-pill badge-success">No ad hominem</span>
            <span v-else class="badge badge-pill badge-danger">Ad hominem</span>
          </div>
          <div class="col-md-auto" v-text="query.query"></div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";

Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import axios from "axios";

export default {
  name: "app",
  components: {},
  data() {
    return {
      current: "",
      oldQueries: [
      ]
    };
  },
  methods: {
    call: function() {
      console.log(this.current);
      var _this = this;

      var bodyFormData = new FormData();
      bodyFormData.set("par", this.current);

      axios({
        method: "post",
        url: "http://localhost:5000/predict",
        data: bodyFormData,
        config: { headers: { "Content-Type": "multipart/form-data" } }
      }).then(function(response) {
        console.log(response)
        _this.oldQueries.unshift({ query: _this.current, result: response.data[0][1] });
        _this.current = "";
      });
    }
  },
  mounted() {}
};
</script>

<style lang="scss">
.pad {
  margin-top: 15px;
}

body,
html {
  height: 100%;
}

.container {
  height: 100%;
  width: 100%;
}
.columns {
  height: 100%;
}
</style>
