<template>
  <v-card :loading="loading" class="mx-auto my-12" max-width="850">
    <template slot="progress">
      <v-progress-linear
        :indeterminate="true"
        color="indigo"
        height="4"
      ></v-progress-linear>
    </template>
    <template v-if="!loading">
      <v-img v-if="book.image" height="500" :src="book.image" contain></v-img>
      <v-divider></v-divider>
      <v-card-title>{{ book.title }}</v-card-title>
      <v-card-subtitle>
       <book-author :id="book.author"></book-author>
      </v-card-subtitle>
      <v-card-text>
        <v-chip>{{ book.genre }}</v-chip>
        <div
          v-text="book.summary"
          class="my-8 indigo--text text--darken-4"
        ></div>
      </v-card-text>
      <v-card-actions>
        <instance-list :id="book.id"></instance-list>
      </v-card-actions>
    </template>
  </v-card>
</template>
  
</v-card> 
</template>

<script>
import BookAuthor from '~/components/buttons/BookAuthor.vue';
import instanceList from "~/components/lists/instanceList.vue";
export default {
  components: { instanceList, BookAuthor },
  name: "BookDetail",
  data() {
    return {
      loading: true,
    };
  },
  computed: {
    book() {
      return this.$store.state.library.detail;
    },
  },
  async mounted() {
    const type = "books";
    const id = this.$route.params.id;
    const detailObj = { type, id };
    await this.$store.dispatch("library/fetchDetail", detailObj);
    this.loading = false;
  },
};
</script>

<style>
</style>