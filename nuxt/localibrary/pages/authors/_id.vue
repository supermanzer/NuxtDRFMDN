<template>
  <v-card :loading="loading" class="mx-auto my-12">
    <template slot="progress">
      <v-progress-linear
        :indeterminate="true"
        color="indigo"
        height="4"
      ></v-progress-linear>
    </template>
    <template v-if="!loading">
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
    </template>
  </v-card>
</template>

<script>
import { mapState } from "vuex";
import twoLines from "~/components/lists/twoLines.vue";
export default {
  components: { twoLines },
  name: "AuthorDetails",
  data() {
    return {
      loading: true,
    };
  },
  computed: mapState({
    author: (state) => state.library.detail,
  }),
  async mounted() {
    const type = "authors";
    const id = this.$route.params.id;
    const detailObj = { type, id };
    await this.$store.dispatch("library/fetchDetail", detailObj);
    this.loading = false;
  },
};
</script>

<style>
</style>