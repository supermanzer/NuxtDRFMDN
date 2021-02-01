<template>
  <div>
    <h1 class="text-h2 py-5">Book List</h1>
    <v-divider></v-divider>
    <p class="text-subtitle">
      We currently have {{ books.count }} books at this library. Please review
      the list of copies for each book to determine which ones are currently
      available
    </p>
    <ext-data-table
      v-if="loaded"
      :headers="headers"
      :records="books.results"
      :pageCount="pageCount"
      @table-change="sortTable"
      @page-change="changePage"
    >
    </ext-data-table>
  </div>
</template>

<script>
import { mapState } from "vuex";
import extDataTable from "~/components/tables/extDataTable.vue";
export default {
  components: { extDataTable },
  name: "BookList",
  computed: {
    ...mapState({
      books: (state) => state.library.books,
    }),
    pageCount() {
      return this.books.count / this.books.results.length;
    },
    loaded() {
      return this.books.hasOwnProperty("results");
    },
  },
  methods: {
    fetchBooks(modifiers = {}) {
      this.$store.dispatch("library/fetchData", { type: "books", modifiers });
    },
    refreshBooks() {
      this.fetchBooks();
    },
    sortTable(options) {
      this.fetchBooks(options);
    },
    changePage(page) {
      this.fetchBooks({ page });
    },
  },
  mounted() {
    // I just want to keep things fresh.  You know?
    this.refreshBooks();
  },
  data() {
    return {
      headers: [
        { text: "Title", value: "title" },
        { text: "Author", value: "author" },
        { text: "Genre", value: "genre" },
      ],
      options: {},
    };
  },
};
</script>

<style>
</style>