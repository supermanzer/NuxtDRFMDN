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
      :headers="headers"
      :records="books.results"
      :page="page"
      :pageCount="pageCount"
      :sync="options"
    >
    </ext-data-table>
    <!-- <v-data-table
      :headers="headers"
      :items="books.results"
      hide-default-footer
      :server-items-length="books.count"
    >
    </v-data-table> -->
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
  },
  methods: {
    refreshBooks() {
      this.$store.dispatch("library/fetchData", "books");
    },
  },
  created() {
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
      page: 1,
      options: {},
    };
  },
};
</script>

<style scoped>
</style>