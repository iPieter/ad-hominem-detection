<template>
  <div class="mt-4">
    <p>This website was created as a project for the course Knowledge and the Web by prof. Bettina Berendt at KU Leuven and is written and maintained by:</p>
    <ul>
      <li>Eric Massip</li>
      <li>Murilo Cunha</li>
      <li>
        <a href="mailto:pieter.delobelle@student.kuleuven.be">Pieter Delobelle</a>
      </li>
    </ul>
    <p>
      Feel free to contact us for questions and/or suggestions. For bugs, please use
      <a
        href="https://github.com/iPieter/G0B34a_knowledge_and_the_web/issues"
      >the issue tracker on GitHub</a>.
    </p>
  </div>
</template>

<script>
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";

Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

export default {
  name: "about",
  components: {},
  methods: {
    mounted() {}
  }
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

img {
  display: block;
  align-self: center;
}
</style>
