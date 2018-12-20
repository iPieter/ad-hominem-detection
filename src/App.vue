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
            <span v-if="query.result < 0.3" class="badge badge-pill badge-success">No ad hominem</span>
            <span v-else-if="query.result < 0.78" class="badge badge-pill badge-warning">Doubt</span>
            <span v-else class="badge badge-pill badge-danger">Ad hominem</span>
            <p class="text-secondary" v-text="Math.round(query.result*100) + '%'"></p>
          </div>
          <div class="col-md-9">
            <p v-text="query.query"></p>
          </div>
        </div>
        <div class="row border-top pt-2 text-hover" v-if="!(query.id in feedbacks)">
          <div class="col-md-6">
            <a href="#" class v-on:click="feedback(query.id, query.query, 0)">
              <i class="far fa-flag"></i> Label as negative
            </a>
          </div>
          <div class="col-md-6">
            <a href="#" class v-on:click="feedback(query.id, query.query, 1)">
              <i class="fas fa-flag"></i> Label as an ad hominem
            </a>
          </div>
        </div>
        <div class="row border-top pt-2 text-hover" v-else>
          <div class="col-md-12">
            Labeling this paragraph impacted the network by 
            <b v-text="Math.round(feedbacks[query.id]*1000)/1000"></b>.
          </div>
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
      index: 0,
      oldQueries: [],
      feedbacks: {}
    };
  },
  methods: {
    feedback: function(id, query, label) {
      var _this = this;

      var bodyFormData = new FormData();
      bodyFormData.set("par", query);
      bodyFormData.set("label", label);

      axios({
        method: "post",
        url: "http://localhost:5000/learn",
        data: bodyFormData,
        config: { headers: { "Content-Type": "multipart/form-data" } }
      }).then(function(response) {
        console.log(response);
        Vue.set(_this.feedbacks, id, response.data)
      });
    },
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
        console.log(response);
        _this.oldQueries.unshift({
          id: _this.index++,
          query: _this.current,
          result: response.data[0][1]
        });
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

.text-hover:not(:hover) {
  opacity: 0.6;
}
</style>
