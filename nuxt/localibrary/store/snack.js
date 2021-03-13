/**
 * store/snack.js
 *
 * This file defines the snack module in the Vuex store for this application.
 * These objects pertain to the actions, text, and display of the snackbar
 * component within the application.  The intent is that we should be able
 * to trigger the display of any sort of snackbar we want without needing
 * to add the component in each page in which we wish it to appear.
 *
 * @returns store objects for snack module
 */

const state = () => ({
  text: "",
  actions: {},
  timeout: 1000,
  classnames: ""
});

const getters = {};

const mutations = {
  SET_SNACK(state, { text, classname }) {
    state.text = text;
    if (classname !== undefined) {
      state.classname = classname;
    }
  }
};

const actions = {};

export default { state, getters, mutations, actions };
