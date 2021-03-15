<!--
  components/buttons/AuthorOverflow.vue

  An overflow button element that allows users to select an author
-->
<template>
  <v-select
    :items="authors"
    item-text="display_name"
    item-value="id"
    v-model="author"
    @input="emitAuthor"
    hide-details
    class="pa-0"
    label="Filter by Author"
  >
  </v-select>
</template>

<script>
export default {
  name: "AuthorOverflow",
  computed: {
    authors() {
      if (this.$store.state.library.authors.length !== 0) {
        return [{ id: null, display_name: "------" }].concat(
          this.$store.state.library.authors.results
        );
      }
      return [];
    },
  },
  data() {
    return {
      author: null,
    };
  },
  methods: {
    emitAuthor() {
      this.$emit("select", { id: this.author });
    },
    loadAuthors() {
      this.$store.dispatch("library/fetchData", {
        type: "authors",
        modifiers: {},
      });
    },
  },
  created() {
    if (this.authors.length === 0) {
      this.loadAuthors();
    }
  },
};
</script>

<style>
</style>
