<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <nav-list-item
          v-for="(item, i) in items"
          :key="i"
          :item="item"
          :i="i"
          :mini="miniVariant"
        ></nav-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon>mdi-{{ `chevron-${miniVariant ? "right" : "left"}` }}</v-icon>
      </v-btn>

      <v-toolbar-title v-text="title" />
    </v-app-bar>
    <v-main>
      <v-container class="mx-12">
        <nuxt />
      </v-container>
    </v-main>

    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import navListItem from "~/components/lists/navListItem.vue";
export default {
  components: { navListItem },
  data() {
    return {
      clipped: true,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: "mdi-home",
          title: "Home",
          to: "/",
        },
        {
          icon: "mdi-book-open-page-variant",
          title: "Books",
          to: { name: "books" },
        },
        {
          icon: "mdi-book-edit",
          title: "Authors",
          to: { name: "authors" },
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Local Library",
    };
  },
};
</script>
