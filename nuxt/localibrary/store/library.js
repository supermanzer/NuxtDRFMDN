/**
 * store/library.js
 * Definig a namespaced store module for data from the library API
 */

// CONSTANTS
const rootUrls = {
  authors: "authors/",
  books: "books/",
  instances: "book-instances/",
  genres: "genres/",
  borrowed: "borrowed/"
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
  available: [],
  headers: {}
});

const mutations = {
  SET_DATA(state, payload) {
    if (state.hasOwnProperty(payload.type)) {
      state[payload.type] = payload.data;
    }
  },
  SET_HEADERS(state, payload) {
    state.headers = payload;
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
   *
   * @param {String} type The type of records to search
   * @param {String} search The term we want to search by
   */
  async searchData({ commit }, { type, search }) {
    let data = await this.$axios.$get(rootUrls[type], { params: { search } });
    commit("SET_DATA", { type, data });
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

  /**
   * Simply get the record we need.  Keeping this in the store
   * since it uses the URLs and keeps our data fetching in one place.
   * @param {string} type The type of record we are fetching
   * @param {Number} id The ID for this particular record
   */
  async fetchDetail({ commit }, { type, id }) {
    let url = `${rootUrls[type]}${id}`;
    let data = await this.$axios.$get(url);
    return data;
  },

  /**
   * Use the DRF OPTIONS response to parse headers for tables and forms (labels)
   * @param {String} type The type of records for which we want headers
   * @param {Number} id If we are fetching headers for a detail, the ID
   */
  async fetchHeaders({ commit }, { type, id = false }) {
    let url = id ? `${rootUrls[type]}${id}` : rootUrls[type];
    let verb = id ? "PUT" : "POST";
    let data = await this.$axios.$options(url);
    commit("SET_HEADERS", data.actions[verb]);
  }
};

const getters = {
  /**
   * Reformat headers to match the array expected by Vuetify data table
   * @param {Object} state library state
   */
  getTableHeaders: state => {
    var headers = [];
    for (const [k, v] of Object.entries(state.headers)) {
      // Screening out values we don't want to see on the table
      if (["url", "id"].indexOf(k) === -1) {
        headers.push({
          text: v.label,
          value: k,
          align: "start",
          sortable: true
        });
      }
    }
    // Adding an actions column
    headers.push({ text: "", value: "actions", sortable: false });
    return headers;
  }
};
export { state, mutations, actions, getters };
