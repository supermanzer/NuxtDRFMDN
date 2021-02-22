<template>
  <v-list-item>
    <v-list-item-icon>
      <v-icon>mdi-book</v-icon>
    </v-list-item-icon>
    <v-list-item-content>
      <v-list-item-title :class="getClass(instance)">
        {{ instance.inst_status }}
      </v-list-item-title>
      <v-list-item-subtitle v-if="instance.due_date">
        <span class="fot-weight-bold">Due Back:</span>
        {{ instance.due_date }}
      </v-list-item-subtitle>
      <v-list-item-subtitle>
        <span class="mr-4">Publisher: {{ instance.imprint }}</span>
        <span class="ml-4">ID: {{ instance.id }}</span>
      </v-list-item-subtitle>
    </v-list-item-content>

    <v-list-item-action>
      <v-icon v-if="loggedIn"> mdi-book-plus </v-icon>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "InstanceItem",
  props: {
    instance: { type: Object, required: true },
  },
  computed: mapState({
    loggedIn: (state) => state.auth.loggedIn,
  }),
  methods: {
    getClass(inst) {
      const colors = {
        a: "green--text text--darken-2",
        o: "amber--text text--darken-2",
        r: "red--text",
        m: "red--text text--darken-4",
      };
      return colors[inst.status];
    },
  },
};
</script>

<style>
</style>