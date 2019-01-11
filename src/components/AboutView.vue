<template>
  <div>
    <h1 class="mt-4" id="detecting-ad-hominem-attacks">Detecting ad hominem attacks</h1>
    <p>
      <em>This project was for the 2018-2019 course ‘Knowledge and the Web’ at KU Leuven.</em>
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
        class="figure-img img-fluid rounded col-8 mx-auto"
        src="network.png"
        alt="Network description"
      >
      <figcaption class="figure-caption text-center">Network description</figcaption>
    </figure>
    <p>The network had the following confusion matrix as output, when it was trained on approximately 20k paragraphs and tested on 8018 paragraphs.</p>
    <figure class="figure col-12">
      <img
        class="figure-img img-fluid rounded col-5 mx-auto"
        src="conf_matrix.png"
        alt="Confusion matrix"
      >
      <figcaption class="figure-caption text-center">Confusion matrix</figcaption>
    </figure>
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
