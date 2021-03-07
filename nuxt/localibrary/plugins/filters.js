/**
 * plugins/filters.js
 * Definig global filters for use in all app components
 */

import Vue from "vue";

Vue.filter("currency", function(val) {
  var return_val = `$${val}`;
  var idx = return_val.indexOf(".");
  if (idx < 0) {
    return_val += ".00";
  } else if (return_val.substring(idx).length <= 2) {
    return_val += "0";
  }
  return return_val;
});
