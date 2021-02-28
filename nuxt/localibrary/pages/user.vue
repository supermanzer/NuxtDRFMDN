<template>
  <div class="my-12 mx-auto">
    <p class="text-h1">Hi {{ user.first_name }} {{ user.last_name }}</p>
    <v-divider></v-divider>
    <div class="light-blue lighten-4 my-6 pa-4">
      <!-- TODO:  Add custom model annotation to sum up late fees for each user and include here -->
      <p class="text-h4">Coming Soon</p>
      <p>
        Section detailing # of overdue books and total late fees owed by patron
      </p>
    </div>
    <template v-if="loading">
      <v-progress-linear
        indeterminate
        color="cyan darken-1"
      ></v-progress-linear>
    </template>
    <div class="my-6" v-else>
      <user-books :books="books.current" :headers="headers">
        <template v-slot:title>
          <span class="text-h4">Your current books</span>
        </template>
      </user-books>
    </div>
    <div class="my-6">
      <user-books :books="books.historic" :headers="headers">
        <template v-slot:title>
          <span class="text-h4">Your previous books</span>
        </template>
      </user-books>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserBooks from "~/components/user/UserBooks.vue";
export default {
  components: { UserBooks },
  name: "UserProfile",
  computed: mapState({
    books: (state) => state.library.books,
    user: (state) => state.auth.user,
  }),
  data() {
    return {
      loading: true,
      headers: [
        {
          text: "Book",
          value: "copy.book",
          sortable: true,
          align: "start",
        },
        {
          text: "Checked Out",
          value: "date_checked_out",
          sortable: true,
          align: "start",
        },
        {
          text: "Due Date",
          value: "due_date",
          sortable: true,
          align: "start",
        },
        {
          text: "Late Fee",
          value: "late_fee",
          sortable: true,
          align: "start",
        },
      ],
    };
  },
  methods: {
    ...mapActions({
      getBooks: "library/fetchMyBooks",
    }),
  },
  async created() {
    await this.getBooks();
    this.loading = false;
  },
};
</script>

<style>
</style>