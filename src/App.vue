<template>
  <div id="app">
    <div class="border-bottom py-2">
      <ul class="container nav justify-content-center nav-fill">
        <li class="nav-item d-none d-sm-block">
          <router-link to="/" class="navbar-brand mb-0 h1">Fallacy detection</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about" class="nav-link" href="/about">About</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/contact" class="nav-link" href="/contact">Contact</router-link>
        </li>
        <li class="nav-item d-none d-sm-block">
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
Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import axios from "axios";

export default {
  name: "app",
  components: {},
  data() {
    return {};
  },
  methods: {},
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
