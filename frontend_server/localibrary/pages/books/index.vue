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
    >
      <template slot="table-top">
        <v-row>
          <v-col cols="12" sm="5">
            <p class="text-h4">Search Books</p>
          </v-col>
          <v-col cols="12" sm="7">
            <v-text-field
              v-model="search"
              label="Search Term"
              @keyup="searchBooks"
            ></v-text-field>
          </v-col>
        </v-row>
      </template>
      <template v-slot:table-actions="slotProps">
        <v-btn
          color="primary"
          icon
          nuxt
          :to="{ name: 'books-id', params: { id: slotProps.item.id } }"
        >
          <v-icon>mdi-details</v-icon>
        </v-btn>
      </template>
    </ext-data-table>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import extDataTable from "~/components/tables/extDataTable.vue";
export default {
  components: { extDataTable },
  name: "BookList",
  computed: {
    ...mapState({
      books: (state) => state.library.books,
    }),
    ...mapGetters({
      headers: "library/getTableHeaders",
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
    searchBooks() {
      this.$store.dispatch("library/searchData", {
        type: "books",
        search: this.search,
      });
    },
  },
  mounted() {
    // I just want to keep things fresh.  You know?
    if (this.books instanceof Array) {
      this.refreshBooks();
      this.$store.dispatch("library/fetchHeaders", { type: "books" });
    }
  },
  data() {
    return {
      search: "",
    };
  },
};
</script>

<style>
</style>