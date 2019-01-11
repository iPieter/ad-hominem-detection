<template>
  <div id="app">
    <div class="border-bottom py-2">
      <ul class="container nav justify-content-center nav-fill">
        <li class="nav-item">
          <router-link to="/" class="navbar-brand mb-0 h1">Fallacy detection</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about" class="nav-link" href="/about">About</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/contact" class="nav-link" href="/contact">Contact</router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/iPieter/G0B34a_knowledge_and_the_web">
            <i class="fab fa-github"></i>
            View on Github
          </a>
        </li>
        <li class="nav-item">
          <router-link
            to="/"
            tag="button"
            type="button"
            class="btn btn-outline-primary"
            href="/"
          >Demo</router-link>
        </li>
      </ul>
    </div>

    <div class="container">
      <router-view class="view"></router-view>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import FallacyView from "./components/FallacyView";
import AboutView from "./components/AboutView";
Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import axios from "axios";

export default {
  name: "app",
  components: {
    FallacyView
  },
  data() {
    return {
      current: "",
      index: 0,
      oldQueries: [],
      feedbacks: {},
      examples: [
        "You are from the United States, so you could never understand what it's like to live in a country like that.",
        "another test"
      ]
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
        Vue.set(_this.feedbacks, id, response.data);
      });
    },
    call: function(example = "") {
      if (example != "") this.current = example;
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
