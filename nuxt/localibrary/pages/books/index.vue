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
      ref="table"
      v-if="loaded"
      :headers="headers"
      :records="books.results"
      :pageCount="books.page_count"
      @table-change="sortTable"
    >
      <template slot="table-top">
        <v-row>
          <v-col cols="12" sm="5">
            <p class="text-h4">Search/Filter Books</p>
          </v-col>
          <v-col cols="12" sm="7">
            <v-text-field
              v-model="search"
              label="Search Term"
              @keyup="sortTable"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="11">
            <v-toolbar dense v-if="filters">
              <author-overflow @select="authorListen"></author-overflow>
              <v-divider vertical class="mx-1"></v-divider>
              <genre-select @select="genreListen"></genre-select>
            </v-toolbar>
          </v-col>
          <v-col cols="12" sm="1">
            <v-tooltip left>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  v-bind="attrs"
                  v-on="on"
                  @click="toggleFilters"
                  elevation="2"
                >
                  <v-icon>mdi-tune</v-icon>
                </v-btn>
              </template>
              <span>Show/Hide Filter Controls</span>
            </v-tooltip>
          </v-col>
        </v-row>
      </template>
      <template v-slot:table-actions="slotProps">
        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              icon
              nuxt
              v-on="on"
              v-bind="attrs"
              :to="{ name: 'books-id', params: { id: slotProps.item.id } }"
            >
              <v-icon>mdi-magnify</v-icon>
            </v-btn>
          </template>
          <span>View Book Details</span>
        </v-tooltip>
      </template>
    </ext-data-table>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import AuthorOverflow from "~/components/buttons/AuthorOverflow.vue";
import extDataTable from "~/components/tables/extDataTable.vue";
export default {
  components: { extDataTable, AuthorOverflow },
  name: "BookList",
  computed: {
    ...mapState({
      books: (state) => state.library.books,
    }),
    ...mapGetters({
      headers: "library/getTableHeaders",
    }),
    loaded() {
      return this.books.hasOwnProperty("results");
    },
  },
  methods: {
    fetchBooks(modifiers = {}) {
      this.$store.dispatch("library/fetchData", { type: "books", modifiers });
      this.$store.dispatch("library/fetchHeaders", { type: "books" });
    },
    refreshBooks() {
      this.fetchBooks();
    },
    sortTable() {
      let options = this.$refs.table.options;
      options["search"] = this.search;
      this.fetchBooks(options);
    },
    searchBooks() {
      this.$store.dispatch("library/searchData", {
        type: "books",
        search: this.search,
      });
    },
    authorListen(e) {
      let options = this.$refs.table.options;
      options["author"] = e.id;
      this.fetchBooks(options);
    },
    genreListen(e) {
      let options = this.$refs.table.options;
      options["genre"] = e.id;
      this.fetchBooks(options);
    },
    toggleFilters() {
      this.filters = !this.filters;
      if (!this.filters) {
        ["genre", "author"].forEach((e) => delete this.$refs.table.options[e]);
        this.fetchBooks();
      }
    },
  },
  data() {
    return {
      search: "",
      filters: false,
    };
  },
  mounted() {
    this.fetchBooks();
  },
};
</script>

<style>
</style>