/**
 * plugins/directives.js
 *
 * Registry of custom Vue directives
 * Custom Vue directives let you add custom functionaity and manipulation to the elements rendered
 * The keys determine where in the lifecycle the function is exicuted and we can take some action
 * based on that.
 */

import Vue from "vue";

Vue.directive("new", {
  inserted: function(el) {
    // DO STUFF HERE
    el.classList.add("pulse");
    console.log(el);
  }
});
