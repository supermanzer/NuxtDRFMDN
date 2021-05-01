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
        Born: {{ author.date_of_birth|niceDate }} - Died: {{ author.date_of_death|niceDate }}
      </v-card-subtitle>
      <v-card-text>
        <author-book-list :id="author.id"></author-book-list>
      </v-card-text>
    </template>
  </v-card>
</template>

<script>
import { mapState } from "vuex";
import AuthorBookList from '~/components/lists/AuthorBookList.vue';
import twoLines from "~/components/lists/twoLines.vue";
export default {
  components: { twoLines, AuthorBookList },
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