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
const apiObject = ({ sortBy, sortDesc, page, ...args }) => {
  // removing unwanted properties
  ["groupBy", "groupDesc", "itemsPerPage", "multiSort", "mustSort"].forEach(
    e => delete args[e]
  );
  var result = args;
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
  headers: {},
  detail: {}
});

const mutations = {
  SET_DATA(state, payload) {
    if (state.hasOwnProperty(payload.type)) {
      state[payload.type] = payload.data;
    }
  },
  SET_HEADERS(state, payload) {
    state.headers = payload;
  },
  SET_DETAIL(state, payload) {
    state.detail = payload;
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
    commit("SET_DETAIL", data);
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
  },

  /**
   * Check out an instance of a book
   * @param {Number} book The ID for the book this copy is related to
   * @param {Object} payload The data needed to check out a book
   */
  async checkoutCopy({ dispatch }, { book, payload }) {
    let url = `${rootUrls.borrowed}`;
    this.$axios.post(url, payload).then(() => {
      dispatch("fetchDetail", { type: "books", id: book });
    });
  },
  /**
   *  Return a checked out book and update user books list
   * @param {Number} book The id of the copy we wish to return
   */
  returnCopy({ dispatch }, { book }) {
    const url = `${rootUrls.borrowed}${book}/`;
    let today = new Date().toISOString();
    today = today.substring(0, today.indexOf("T"));
    const payload = { date_returned: today };
    this.$axios.patch(url, payload).then(() => {
      dispatch("fetchMyBooks");
    });
  },

  /**
   * Return lists of current and historic books checked out by authenticated user
   */
  async fetchMyBooks({ commit }) {
    let url = `${rootUrls.borrowed}user_books/`;
    let data = await this.$axios.$get(url);
    commit("SET_DATA", { type: "books", data });
  },
  /**
   * Similar to fetchDetail, but returns the object to the caller
   * @param {String} type The type of record to be fetched
   * @param {Number} id The id for the individual record
   * @param {String|Boolean} suffix Any suffix we need to add to the url
   */
  async fetchAction({commit}, {type, id, suffix = false}) {
    let url = suffix ? `${rootUrls[type]}${id}/${suffix}` : `${rootUrls[type]}${id}`
    return await this.$axios.$get(url)
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
