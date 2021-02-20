<template>
  <div>
    <v-card class="mx-auto" max-width="1420">
      <v-img
        class="white--text align-end"
        height="700"
        src="https://images.pexels.com/photos/3952071/pexels-photo-3952071.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
        gradient="to right, rgba(0,0,0,.4), rgba(0,0,0,0.1)"
      >
        <v-card-title class="text-md-h2">
          Welcome to your Local Library
        </v-card-title>
      </v-img>
      <v-card-subtitle> Resources </v-card-subtitle>
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="3" class="rb">
            <two-lines>
              <template v-slot:title>Authors</template>
              <template v-slot:subtitle>
                We currently have books from
                {{ num_authors }} authors
              </template>
            </two-lines>
          </v-col>
          <v-col cols="12" sm="3" class="rb">
            <two-lines>
              <template v-slot:title>Books</template>
              <template v-slot:subtitle>
                We currently have {{ num_books }} books
              </template>
            </two-lines>
          </v-col>
          <v-col cols="12" sm="3" class="rb">
            <two-lines>
              <template v-slot:title>Copies</template>
              <template v-slot:subtitle>
                Of the {{ num_books }} books, we currently have
                {{ num_instances }} copies
              </template>
            </two-lines>
          </v-col>
          <v-col cols="12" sm="3">
            <two-lines>
              <template v-slot:title>Genres</template>
              <template v-slot:subtitle>
                We currently have books in {{ num_genres }} Genres
              </template>
            </two-lines>
          </v-col>
        </v-row>
        <v-row class="pt-6 mt-6">
          <v-col cols="12" sm="4" offset-sm="4">
            <two-lines>
              <template v-slot:title>Books Available</template>
              <template v-slot:subtitle>
                There are {{ num_instances_available }} copies ready to be
                checked out
              </template>
            </two-lines>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { mapState } from "vuex";
import twoLines from "~/components/lists/twoLines.vue";
export default {
  components: { twoLines },
  name: "HomePage",
  head: {
    title: "Welcome",
    meta: [
      {
        hid: "description",
        name: "description",
        content: "The home page for your Local Library",
      },
    ],
  },
  data() {
    return {
      models: ["authors", "books", "instances", "genres"],
    };
  },
  methods: {
    loadData() {
      this.models.forEach((model) =>
        this.$store.dispatch("library/fetchData", {
          type: model,
          modifiers: {},
        })
      );
    },
  },
  mounted() {
    this.loadData();
    this.$store.dispatch("library/checkAvailable");
  },
  computed: mapState({
    num_books: (state) => state.library.books.count,
    num_instances: (state) => state.library.instances.count,
    num_instances_available: (state) => state.library.available.count,
    num_authors: (state) => state.library.authors.count,
    num_genres: (state) => state.library.genres.count,
  }),
};
</script>

<style>
.rb {
  border-right: 2px #aaa solid;
}
</style>