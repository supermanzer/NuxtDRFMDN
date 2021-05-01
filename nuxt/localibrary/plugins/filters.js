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

/**
 * Returns Date().toDateString() based on
 * ISO date strings
 */
Vue.filter('niceDate', function(val) {
  if (val != null) {
    const [y, m, d] = val.split("-").map(a => Number(a));
    const myD = new Date(y, m - 1, d); // Month is an index in this case so starts at 0....weird
    return myD.toDateString();
  }
  return ''
  
})
