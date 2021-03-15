/**
 * plugins/directives.js
 *
 * Registry of custom Vue directives
 */

import Vue from "vue";

Vue.directive("new", {
  inserted: function(el) {
    // DO STUFF HERE
    el.classList.add("pulse");
    console.log(el);
  }
});
