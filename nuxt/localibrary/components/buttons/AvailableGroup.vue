<!--
    components/buttons/AvailableGroup.vue

    This component defines a button group used to toggle the list of books returned between
    only those with available copies and all books
-->

<template>
  <v-btn-toggle mandatory v-model="books_choice" @change="emitChoice">
    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-bind="attrs" v-on="on">All</v-btn>
      </template>
      <span>Show all books</span>
    </v-tooltip>
    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-bind="attrs" v-on="on">Available</v-btn>
      </template>
      <span>Only show books with available copies</span>
    </v-tooltip>
  </v-btn-toggle>
</template>

<script>
export default {
  name: "AvailableGroup",

  data() {
    return {
      books_choice: 0,
      choices: {
        0: "",
        1: "a",
      },
    };
  },
  methods: {
    emitChoice() {
      this.$emit("choice", this.choices[this.books_choice]);
    },
  },
};
</script>

<style>
</style>