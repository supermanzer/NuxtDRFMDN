<template>
  <v-data-table
    :headers="headers"
    :items="books"
    :items-per-page="items_per_page"
    :search="search"
    no-data-text="No books at present"
    no-results-text="No books found. Try widening your search"
  >
    <template v-slot:top>
      <v-toolbar color="grey lighten-3" flat>
        <v-toolbar-title>
          <slot name="title"></slot>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          v-show="showSearch"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        <v-btn color="light-blue" @click="toggleSearch" icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>
    </template>
    <template v-slot:item.due_date="{ item }">
      <template v-if="item.copy.overdue && item.date_returned == null">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-chip color="red darken-2" dark v-bind="attrs" v-on="on">
              {{ item.due_date }}
            </v-chip>
          </template>
          <span>Book Overdue! Return immediately</span>
        </v-tooltip>
      </template>
      <template v-else>
        {{ item.due_date }}
      </template>
    </template>
    <template v-slot:item.late_fee="{ item }">
      {{ item.late_fee | currency }}
    </template>
    <template v-slot:item.actions="{ item }">
      <return-book :id="item.id"></return-book>
    </template>
  </v-data-table>
</template>

<script>
import ReturnBook from "../forms/returnBook.vue";
export default {
  name: "UserBooks",
  components: {
    ReturnBook,
  },
  props: {
    books: { type: Array, required: true },
    headers: { type: Array, required: true },
  },
  data() {
    return {
      items_per_page: 10,
      search: "",
      showSearch: false,
    };
  },
  methods: {
    toggleSearch() {
      this.showSearch = !this.showSearch;
      this.search = "";
    },
  },
};
</script>

<style>
</style>