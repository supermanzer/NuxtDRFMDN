<template>
  <div class="text-center" v-if="loggedIn">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-list-item v-bind="attrs" v-on="on">
          <v-list-item-title>Hi {{ user.first_name }}</v-list-item-title>
        </v-list-item>
      </template>
      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
        <v-list-item nuxt :to="{ name: 'logout' }">Log Out</v-list-item>
      </v-list>
    </v-menu>
  </div>
  <div v-else>
    <v-list-item nuxt :to="{ name: 'login' }">
      <v-list-item-title>Log In</v-list-item-title>
    </v-list-item>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "UserMenu",
  computed: mapState({
    user: (state) => state.auth.user,
    loggedIn: (state) => state.auth.loggedIn,
  }),
  data() {
    return {
      items: [{ title: "Things" }, { title: "Stuff" }],
    };
  },
};
</script>

<style>
</style>