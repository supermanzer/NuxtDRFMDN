/**
 * store/library.js
 * Definig a namespaced store module for data from the library API
 */

const rootUrls = {
  authors: "authors/",
  books: "books/",
  instances: "book-instances/",
  genres: "genres/"
};

const state = () => ({
  authors: [],
  books: [],
  instances: [],
  genres: [],
  available: []
});

const mutations = {
  SET_DATA(state, payload) {
    if (state.hasOwnProperty(payload.type)) {
      state[payload.type] = payload.data;
    }
  }
};

const actions = {
  /**
   * Generic API data fetching
   * @param {String} type The type of records to fetch
   */
  async fetchData({ commit }, type) {
    if (rootUrls.hasOwnProperty(type)) {
      let data = await this.$axios.$get(rootUrls[type]);
      commit("SET_DATA", { type, data });
    }
  },
  /**
   * checkAvailable
   *
   * Return an object containing the instances whose status is a or Available
   */
  async checkAvailable({ commit }) {
    let url = rootUrls.instances + "?status=a";
    let data = await this.$axios.$get(url);
    let type = "available";
    commit("SET_DATA", { type, data });
  }
};

export { state, mutations, actions };
