<template>
  <div>
    <h1 class="mt-4" id="detecting-ad-hominem-attacks">Computational ad hominem detection</h1>
    <p>
      <b>
        Pieter Delobelle, Murilo Cunha, Eric Massip Cano,
        Jeroen Peperkamp and Bettina Berendt
      </b>
      <br />KU Leuven, Department of Computer Science
      <br />Celestijnenlaan 200A, 3000 Leuven, Belgium
    </p>
    <p>
      <em>
        <a href="/80_paper.pdf">The paper</a> will be presented at
        <a href="http://www.acl2019.org/EN/">ACL 2019</a> during the
        <a
          href="https://sites.google.com/view/acl19studentresearchworkshop/"
        >student research workshop</a>.
      </em>
    </p>
    <p>
      The term “fake news” is associated with journalism that deliberately spreads deceitful or inaccurate information. In the past years, the use of the term has increased drastically, interfering in major areas within a community. The importance is such that Italian schools have implemented “fake news detection” as part of the school curriculum. In the political sphere, it is not uncommon to see allegations of fake news and misinformation. Those calls that often target sources, reporters and organizations, instead of assessing the arguments themselves. This paper will discuss the possibility to
      <strong>detect fallacies</strong>, primarily on the
      <em>ad hominem</em>.
      <em>Ad hominem</em> literally means “to the person”, and the term is used when an argument directs to the person instead of assessing the argument itself.
    </p>
    <p>
      The datasets are sourced from
      <a href="https://github.com/UKPLab/argotario">UKPLab/argotario</a> and
      <a
        href="https://github.com/UKPLab/naacl2018-before-name-calling-habernal-et-al"
      >UKPLab/naacl2018-before-name-calling-habernal-et-al</a>.
    </p>
    <h2 id="classifier">Classifier</h2>
    <p>
      During the project,
      <strong>several classifiers and network architectures</strong> were reviewed. The results are incorporated in the paper. The final, best performing network is a
      <strong>bidirectional GRU</strong> neural network, with the following features:
    </p>
    <ul>
      <li>
        <a href="https://code.google.com/archive/p/word2vec/">Pre-trained</a> word embeddings (
        <a href="https://radimrehurek.com/gensim/models/word2vec.html">word2vec</a>).
      </li>
      <li>Document embeddings.</li>
      <li>
        Part-of-speech tags (
        <a href="http://www.nltk.org/">NLTK</a>).
      </li>
    </ul>
    <p>
      These features are combined into a classification network, resulting in a labeling as
      <em>ad hominem</em> or
      <em>no ad hominem</em>.
    </p>
    <figure class="figure">
      <img
        class="figure-img img-fluid rounded col-md-8 mx-auto"
        src="network.png"
        alt="Network description"
      />
      <figcaption class="figure-caption text-center">Network description</figcaption>
    </figure>
    <p>The network had the following confusion matrix as output, when it was trained on approximately 20k paragraphs and tested on 8018 paragraphs.</p>
    <figure class="figure col-12">
      <img
        class="figure-img img-fluid rounded col-sm-9 col-md-5 mx-auto"
        src="conf_matrix.png"
        alt="Confusion matrix"
      />
      <figcaption class="figure-caption text-center">Confusion matrix</figcaption>
    </figure>

    <h2>Demo architecture</h2>
    <p>
      For this demo website, a
      <a href="http://vuejs.org">Vue.js</a>
      application is served as a frontend. The backend is a bit more complicated, since the presented model requires a reasonably performant machine with around 5 GB RAM. Since this gets expensive quicly, an architecture with a decentral worker system is used, as is illustrarted in the next figure.
    </p>
    <figure class="figure col-12">
      <img
        class="figure-img img-fluid rounded col-md-8 mx-auto"
        src="architecture.png"
        alt="Architecture for this demo"
      />
      <figcaption class="figure-caption text-center">Architecture for this demo</figcaption>
    </figure>
    <p>
      This allows for a small, cheap server to run the broker,
      <a href="http://rabbitmq.com">RabbitMQ</a> in this case, but still handle all requests. We even get load balancing for free!
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
