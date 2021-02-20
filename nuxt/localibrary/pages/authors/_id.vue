<template>
  <v-card>
    <v-card-title primary-title>
      Author: {{ author.last_name }}, {{ author.first_name }}
    </v-card-title>
    <v-divider></v-divider>
    <v-card-subtitle>
      {{ author.date_of_birth }} - {{ author.date_of_death }}
    </v-card-subtitle>
    <v-card-text>
      <two-lines v-for="book in author.books" :key="book.id">
        <template slot="title">
          <v-btn
            color="primary"
            text
            nuxt
            :to="{ name: 'books-id', params: { id: book.id } }"
          >
            {{ book.title }}
          </v-btn>
        </template>
        <template slot="subtitle">
          {{ book.summary }}
        </template>
      </two-lines>
    </v-card-text>
  </v-card>
</template>

<script>
import twoLines from "~/components/lists/twoLines.vue";
export default {
  components: { twoLines },
  name: "AuthorDetails",
  data() {
    return {
      author: {},
      loading: true,
    };
  },
  methods: {
    async fetchAuthor() {
      let id = this.$route.params.id;
      let author = await this.$store.dispatch("library/fetchDetail", {
        type: "authors",
        id,
      });
      this.author = author;
    },
  },
  mounted() {
    this.fetchAuthor();
  },
};
</script>

<style>
</style>