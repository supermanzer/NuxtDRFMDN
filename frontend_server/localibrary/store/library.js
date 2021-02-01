/**
 * store/library.js
 * Definig a namespaced store module for data from the library API
 */

// CONSTANTS
const rootUrls = {
  authors: "authors/",
  books: "books/",
  instances: "book-instances/",
  genres: "genres/"
};

// UTILITY FUNCTIONS
/**
 * Function to alter base URL - performs server side sorting, searching, pagination
 * @param {String} url base URL to be modified
 * @param {Object} modifiers Modifiers (sortBy, page, etc)
 */
const apiUrl = (url, modifiers) => {
  url = url.indexOf("?") === -1 ? url + "?" : url;
  for (const [key, value] of Object.entries(modifiers)) {
    url = `${url}${key}=${value}&`;
  }
  return url.slice(0, -1);
};

/**
 * Translate Vuetify options object into keys: values that match API requirements
 * @param {Object} modifiers The options object returned by paginated/sorted table
 */
const apiObject = ({ sortBy, sortDesc, page }) => {
  var result = {};
  if (sortBy.length === 1 && sortDesc.length === 1) {
    result.ordering = sortDesc[0] ? `-${sortBy[0]}` : sortBy[0];
  }
  result.page = page;
  // console.log(result);
  return result;
};

// STORE OBJECTS
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
  async fetchData({ commit }, { type, modifiers }) {
    var urlObj = {};
    if (rootUrls.hasOwnProperty(type)) {
      if (
        modifiers.hasOwnProperty("sortBy") ||
        modifiers.hasOwnProperty("page")
      ) {
        urlObj = apiObject(modifiers);
      }
      // const url = apiUrl(rootUrls[type], modifiers);
      // console.log(url);
      let data = await this.$axios.$get(rootUrls[type], { params: urlObj });
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
  },

  async fetchDetail({ commit }, { type, id }) {
    let url = `${rootUrls[type]}${id}`;
    let data = await this.$axios.$get(url);
    return data;
  }
};

export { state, mutations, actions };
