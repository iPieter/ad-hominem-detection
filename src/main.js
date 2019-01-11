import Vue from "vue";
import App from "./App.vue";
import FallacyView from "./components/FallacyView";
import AboutView from "./components/AboutView";
import ContactView from "./components/ContactView";
import VueRouter from "vue-router";

Vue.use(VueRouter);

// 2. Define route components
// 3. Create the router
const router = new VueRouter({
  mode: "history",
  base: __dirname,
  routes: [
    { path: "/", component: FallacyView },
    { path: "/about", component: AboutView },
    { path: "/contact", component: ContactView }
  ]
});

// 4. Create extended base Vue with router injected here (all
// children should inherit the same router).
new Vue({
  router,
  el: "#app",
  render: h => h(App)
});
