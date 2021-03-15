<!--
  components/buttons/AuthorOverflow.vue

  An overflow button element that allows users to select an author
-->
<template>
  <v-select
    :items="genres"
    item-text="name"
    item-value="id"
    v-model="genre"
    @input="emitGenre"
    hide-details
    class="pa-0"
    label="Filter by Genre"
  >
  </v-select>
</template>

<script>
export default {
  name: "AuthorOverflow",
  computed: {
    genres() {
      if (this.$store.state.library.genres.length !== 0) {
        return [{ id: null, name: "-----------" }].concat(
          this.$store.state.library.genres.results
        );
      }
      return [];
    },
  },
  data() {
    return {
      genre: null,
    };
  },
  methods: {
    emitGenre() {
      this.$emit("select", { id: this.genre });
    },
    loadGenres() {
      this.$store.dispatch("library/fetchData", {
        type: "genres",
        modifiers: {},
      });
    },
  },
  created() {
    if (this.genres.length === 0) {
      this.loadGenres();
    }
  },
};
</script>

<style>
</style>
