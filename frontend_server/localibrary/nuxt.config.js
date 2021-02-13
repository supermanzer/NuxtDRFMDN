import colors from "vuetify/es5/util/colors";

export default {
  // Disable server-side rendering (https://go.nuxtjs.dev/ssr-mode)
  ssr: false,

  // Target (https://go.nuxtjs.dev/config-target)
  target: "static",

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    titleTemplate: "%s - localibrary",
    title: "localibrary",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" }
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    "@nuxtjs/vuetify",
    "@nuxtjs/composition-api"
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    "@nuxtjs/axios",
    // https://go.nuxtjs.dev/content
    "@nuxt/content",
    //https://auth.nuxtjs.org/guide/setup/
    "@nuxtjs/auth-next",
    //https://www.npmjs.com/package/@nuxtjs/toast
    "@nuxtjs/toast"
  ],

  toast: {
    position: "top-right",
    iconPack: "mdi",
    register: [
      {
        name: "login",
        message: "Log in successful",
        options: {
          duration: 3000,
          theme: "bubble",
          icon: "check-outlilne",
          className: "green--text"
        }
      }
    ]
  },

  // Configuring authentication module: https://auth.nuxtjs.org/api/options
  auth: {
    cookie: {
      prefix: "auth.",
      options: {
        sameSite: "lax"
      }
    },
    strategies: {
      local: {
        scheme: "refresh",
        token: {
          prefix: "token",
          property: "access", // The name of the property in the API response that corresponds to the token value
          // maxAge: 60 * 5, // Corresponds to the lifetime of the token set in the back end
          type: "Bearer" // The Authorization header our API expects
        },
        refreshToken: {
          prefix: "refresh",
          property: "refresh",
          data: "refresh"
          // maxAge: 60 * 60 * 24 * 7
        },
        user: {
          property: false
        },
        endpoints: {
          login: { url: "token/", method: "post" }, // Defining the route we pass username/passwords and get tokens
          refresh: { url: "token/refresh/", method: "post" },
          user: { url: "user/", method: "get" }
        }
      }
    },
    redirect: {
      login: "/login",
      logout: "/",
      callback: "/login",
      home: "/"
    }
  },
  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    baseURL: "http://localhost:9000/api/"
  },

  // Content module configuration (https://go.nuxtjs.dev/config-content)
  content: {},

  // Vuetify module configuration (https://go.nuxtjs.dev/config-vuetify)
  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {}
};
