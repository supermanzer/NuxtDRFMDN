<template>
  <div>
    <p class="text-h2 pt-4">Authors</p>
    <v-divider></v-divider>
    <p class="subtitle pb-5">
      Below are the authors whose works are available through this library
    </p>
    <ext-data-table
      v-if="loaded"
      :headers="headers"
      :records="authors.results"
      :pageCount="pageCount"
      @table-change="changeTable"
    >
      <template slot="table-top">
        <v-row>
          <v-col cols="12" sm="6">
            <p class="text-h4">Search Authors</p>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field
              v-model="search"
              label="Search Term"
              @keyup="searchAuthors"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-divider inset></v-divider>
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
              :to="{ name: 'authors-id', params: { id: slotProps.item.id } }"
            >
              <v-icon>mdi-magnify</v-icon>
            </v-btn>
          </template>
          <span>View Author Details</span>
        </v-tooltip>
      </template>
    </ext-data-table>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import extDataTable from "~/components/tables/extDataTable.vue";
export default {
  components: { extDataTable },
  name: "AuthorsList",
  computed: {
    ...mapState({
      authors: (state) => state.library.authors,
    }),
    ...mapGetters({
      headers: "library/getTableHeaders",
    }),
    loaded() {
      return this.authors.hasOwnProperty("results");
    },
    pageCount() {
      return this.authors.count / this.authors.results.length;
    },
  },
  methods: {
    fetchAuthors(modifiers) {
      this.$store.dispatch("library/fetchData", { type: "authors", modifiers });
    },
    changeTable(options) {
      this.fetchAuthors(options);
    },
    fetchHeaders() {
      this.$store.dispatch("library/fetchHeaders", { type: "authors" });
    },
    searchAuthors() {
      this.$store.dispatch("library/searchData", {
        type: "authors",
        search: this.search,
      });
    },
  },
  mounted() {
    this.fetchAuthors({});
    this.fetchHeaders();
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