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
      <v-img v-if="book.image" height="300" :src="book.image"></v-img>
      <v-card-title>{{ book.title }}</v-card-title>
      <v-card-subtitle>
        <v-btn
          color="grey"
          nuxt
          text
          :to="{ name: 'authors-id', params: { id: book.author.id } }"
          >{{ book.author.last_name }}, {{ book.author.first_name }}</v-btn
        >
      </v-card-subtitle>
      <v-card-text>
        <v-chip>{{ book.genre }}</v-chip>
        <div
          v-text="book.summary"
          class="my-8 indigo--text text--darken-4"
        ></div>
      </v-card-text>
      <v-card-actions>
        {{ num_instances }} Copies, {{ num_available }} Available
        <v-spacer></v-spacer>
        <v-btn icon @click="showInstances = !showInstances">
          <v-icon>{{
            showInstances ? "mdi-chevron-up" : "mdi-chevron-down"
          }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-expand-transition>
        <div v-show="showInstances" class="pa-4">
          <v-divider></v-divider>
          <h3 class="text-h5">Copies</h3>
          <instance-list :instances="book.instances"></instance-list>
        </div>
      </v-expand-transition>
    </template>
  </v-card>
</template>
  
</v-card> 
</template>

<script>
import instanceList from "~/components/lists/instanceList.vue";
export default {
  components: { instanceList },
  name: "BookDetail",
  data() {
    return {
      loading: true,
      showInstances: false,
    };
  },
  computed: {
    book() {
      return this.$store.state.library.detail;
    },
    num_instances() {
      return !this.loading ? this.book.instances.length : 0;
    },
    num_available() {
      return !this.loading
        ? this.book.instances.filter((i) => i.status === "a").length
        : 0;
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