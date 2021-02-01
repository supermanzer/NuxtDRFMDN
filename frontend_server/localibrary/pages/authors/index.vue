<template>
  <ext-data-table
    v-if="loaded"
    :headers="headers"
    :records="authors.results"
    :pageCount="pageCount"
    @table-change="changeTable"
  >
  </ext-data-table>
</template>

<script>
import { mapState } from "vuex";
import extDataTable from "~/components/tables/extDataTable.vue";
export default {
  components: { extDataTable },
  name: "AuthorsList",
  computed: {
    ...mapState({
      authors: (state) => state.library.authors,
    }),
    loaded() {
      return this.authors.hasOwnProperty("results");
    },
    pageCount() {
      return this.authors.count / this.authors.results.length;
    },
  },
  data() {
    return {
      headers: [
        { text: "Last Name", value: "last_name" },
        { text: "First Name", value: "first_name" },
        { text: "Date of Birth", value: "date_of_birth" },
        { text: "Date of Death", value: "date_of_death" },
      ],
    };
  },
  methods: {
    fetchAuthors(modifiers) {
      this.$store.dispatch("library/fetchData", { type: "authors", modifiers });
    },
    changeTable(options) {
      this.fetchAuthors(options);
    },
  },
};
</script>

<style>
</style>