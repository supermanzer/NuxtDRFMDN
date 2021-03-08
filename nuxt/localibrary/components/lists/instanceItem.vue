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
      <template v-if="loggedIn">
        <v-btn
          color="success"
          text
          :disabled="available(instance)"
          @click="checkOut"
        >
          Check out book
          <v-icon> mdi-book-plus </v-icon>
        </v-btn>
      </template>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "InstanceItem",
  props: {
    instance: { type: Object, required: true },
  },
  computed: mapState({
    loggedIn: (state) => state.auth.loggedIn,
    user: (state) => state.auth.user,
  }),
  methods: {
    ...mapMutations({
      snackTime: "snack/SET_SNACK",
    }),
    getClass() {
      const colors = {
        a: "green--text text--darken-2",
        o: "amber--text text--darken-2",
        r: "red--text",
        m: "red--text text--darken-4",
      };
      return colors[this.instance.status];
    },
    available() {
      return this.instance.status != "a";
    },
    async checkOut() {
      const td = new Date();
      const book = this.instance.book_id;
      const payload = {
        copy: this.instance.id,
        date_checked_out: `${td.getFullYear()}-${
          td.getMonth() + 1
        }-${td.getDate()}`,
      };
      await this.$store.dispatch("library/checkoutCopy", { book, payload });
      this.snackTime({ text: "Book checked out", color: "success" });
    },
  },
};
</script>

<style>
</style>