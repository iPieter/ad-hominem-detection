<template>
  <div class="px-2">
    <div class="row mt-3">
      <h1 class="pl-0 col-md-6 offset-md-3">Go on, insult us ...</h1>
    </div>

    <div class="form-group row">
      <textarea class="col-md-6 offset-md-3 form-control" v-model="current" rows="3"></textarea>
    </div>
    <div class="row">
      <button class="btn btn-primary col-md-6 offset-md-3" v-on:click="call()">Analyze</button>
    </div>
    <div class="row mt-3">
      <h2 v-if="oldQueries.length == 0" class="mt-4 pl-0 col-md-6 offset-md-3">Or try an example</h2>
    </div>
    <ul class="list-group row mt-4">
      <li v-for="query in oldQueries" class="list-group-item col-md-6 offset-md-3">
        <div class="row">
          <div class="col-auto mr-auto">
            <span v-if="query.result < 0.3" class="badge badge-pill badge-success">No ad hominem</span>
            <span v-else-if="query.result < 0.78" class="badge badge-pill badge-warning">Doubt</span>
            <span v-else class="badge badge-pill badge-danger">Ad hominem</span>
            <p class="text-secondary" v-text="Math.round(query.result*100) + '%'"></p>
          </div>
          <div class="col">
            <p v-text="query.query"></p>
          </div>
        </div>
        <div class="row border-top pt-2 text-hover" v-if="!(query.id in feedbacks)">
          <div class="col-6">
            <a href="#" class v-on:click="feedback(query.id, query.query, 0)">
              <i class="far fa-flag"></i> Label as negative
            </a>
          </div>
          <div class="col-6">
            <a href="#" class v-on:click="feedback(query.id, query.query, 1)">
              <i class="fas fa-flag"></i> Label as an ad hominem
            </a>
          </div>
        </div>
        <div class="row border-top pt-2 text-hover" v-else>
          <div class="col-12">{{feedbacks[query.id]}}</div>
        </div>
      </li>

      <li
        v-if="oldQueries.length == 0"
        v-for="example in examples"
        class="list-group-item col-md-6 offset-md-3"
      >
        <div class="row">
          <div class="col-md-9">
            <p v-text="example"></p>
          </div>
          <div class="col-auto">
            <button
              type="button"
              class="btn btn-outline-primary"
              v-on:click="call(example)"
            >Test out</button>
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

export default {
  name: "fallacy",
  components: {},
  data() {
    return {
      current: "",
      index: 0,
      id: "",
      oldQueries: [],
      feedbacks: {},
      client: {},
      examples: [
        "Do you want to have a conversation, or do you want to troll?",
        "Fucking idiot!!!!",
        "This is a really nice website :-)",
        "You’ve got an answer to everything haven’t you?"
      ]
    };
  },
  methods: {
    feedback: function(id, query, label) {
      var _this = this;

      this.client.send(
        "/queue/labels",
        {},
        JSON.stringify({
          paragraph: query,
          client: this.id,
          label: label
        })
      );

      Vue.set(
        _this.feedbacks,
        id,
        "Thanks for labeling this as " +
          (label ? "an ad hominem!" : "not an ad hominem!")
      );
    },
    call: function(example = "") {
      if (example != "") this.current = example;

      this.client.send(
        "/queue/fallacies",
        {},
        JSON.stringify({
          paragraph: this.current,
          client: this.id
        })
      );
    }
  },
  mounted() {
    var uuid = require("uuid");
    this.id = uuid.v4();

    let _this = this;

    var ws = new WebSocket("ws://fallacies.ipieter.be/ws/");
    this.client = Stomp.over(ws);
    var on_connect = function() {
      console.log("connected");

      var callback = function(message) {
        // called when the client receives a STOMP message from the server
        if (message.body) {
          let m = JSON.parse(message.body);
          _this.oldQueries.unshift({
            id: _this.index++,
            query: m.paragraph,
            result: m.result[0][1]
          });
          _this.current = "";
        } else {
          alert("got empty message");
        }
      };

      var subscription = _this.client.subscribe(
        "/exchange/amq.direct/" + _this.id,
        callback
      );
      console.log(subscription);
    };
    var on_error = function() {
      console.log("error");
    };
    this.client.connect("fallacies", "yQCxcQ8r", on_connect, on_error, "/");
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
</style>
