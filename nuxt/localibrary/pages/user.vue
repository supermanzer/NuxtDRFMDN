<template>
  <div class="my-12 mx-auto">
    <p class="text-h1">Hi {{ user.first_name }} {{ user.last_name }}</p>
    <v-divider></v-divider>
    <template v-if="loading">
      <v-progress-linear
        indeterminate
        color="cyan darken-1"
      ></v-progress-linear>
    </template>
    <template v-else>
      <v-row class="mt-12">
        <v-col cols="12" sm="12" class="d-flex justify-center center-align">
          <v-text-field v-model="snackText" label="Snack Text"></v-text-field>
          <v-btn color="indigo" class="white--text" @click="snackTime"
            >Show Snack</v-btn
          >
        </v-col>
      </v-row>
      <v-row class="my-6 pa-4">
        <v-col cols="12" sm="12" md="6">
          <two-lines>
            <template v-slot:title>
              <span class="text-h4">Your Current Books</span>
            </template>
            <template v-slot:subtitle>
              You have
              <span class="font-weight-bold">{{ books.current.length }}</span>
              books checked out (see table below)</template
            >
          </two-lines>
        </v-col>
        <v-col cols="12" sm="12" md="6">
          <two-lines>
            <template v-slot:title>
              <span class="text-h4"
                >Late Fees: {{ total_fees | currency }}</span
              >
            </template>
            <template v-slot:subtitle>
              You currently owe {{ total_fees | currency }} in late fees to the
              library
            </template>
          </two-lines>
        </v-col>
      </v-row>

      <div class="my-6">
        <user-books :books="books.current" :headers="headers">
          <template v-slot:title>
            <span class="text-h4">Your current books</span>
          </template>
        </user-books>
      </div>
      <div class="my-6">
        <user-books :books="books.historic" :headers="historic_headers">
          <template v-slot:title>
            <span class="text-h4">Your previous books</span>
          </template>
        </user-books>
      </div>
    </template>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserBooks from "~/components/user/UserBooks.vue";

import TwoLines from "~/components/lists/twoLines.vue";
export default {
  components: { UserBooks, TwoLines },
  name: "UserProfile",
  computed: {
    ...mapState({
      books: (state) => state.library.books,
      user: (state) => state.auth.user,
    }),
    total_fees() {
      const sum_fee = (val, book) => val + book.late_fee;
      var fee = this.books.current.reduce(sum_fee, 0);
      fee = this.books.historic.reduce(sum_fee, fee);
      return fee;
    },
  },
  data() {
    return {
      loading: true,
      snackText: "",
      headers: [
        {
          text: "Book",
          value: "book",
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
        {
          text: "Return",
          value: "actions",
          sortable: false,
          align: "start",
        },
      ],
      historic_headers: [
        {
          text: "Book",
          value: "book",
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
          text: "Date Returned",
          value: "date_returned",
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
    snackTime() {
      this.$store.commit("snack/SET_SNACK", {
        text: this.snackText,
        color: "error",
      });
    },
  },
  async created() {
    await this.getBooks();
    this.loading = false;
  },
};
</script>

<style>
</style>