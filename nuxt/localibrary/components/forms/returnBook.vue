<template>
  <div>
    <v-btn color="cyan" dark small @click.stop="loadOpen">
      <v-icon>mdi-book-arrow-up</v-icon>
    </v-btn>
    <v-dialog v-model="dialog" persistent:overlay="false" max-width="500px">
      <v-card :loading="loading">
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>
        <template v-if="!loading">
          <v-img
            class="white--text align-end gd"
            height="150"
            src="https://images.pexels.com/photos/2846814/pexels-photo-2846814.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
            gradient="to bottom, rgba(0,0,0, 0.2), rgba(0,0,0, 0.6)"
          >
            <v-card-title
              >Your borrowed copy of {{ copy.book }}</v-card-title
            >
          </v-img>
          <v-card-text>
            <p v-if="copy.copy.overdue" class="red--text text-darken-3">
              This book is overdue. Please return immediately to avoid further
              late fees.
            </p>
            <v-form>
              <v-row>
                <v-col
                  cols="12"
                  sm="12"
                  md="6"
                  lg="4"
                  v-for="(field, i) in display_fields"
                  :key="i"
                >
                  <v-text-field
                    readonly
                    :value="copy[field]"
                    :label="headers[field].label"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="grey lighten-1" @click="dialog = false" dark
              >Cancel</v-btn
            >
            <v-spacer></v-spacer>
            <v-btn color="indigo" dark large rounded @click="returnCopy"
              >Return Copy</v-btn
            >
          </v-card-actions>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "ReturnBook",
  props: {
    id: { type: Number, required: true },
  },
  computed: mapState({
    copy: (state) => state.library.detail,
    headers: (state) => state.library.headers,
  }),
  data() {
    return {
      loading: true,
      dialog: false,
      display_fields: [
        "date_checked_out",
        "due_date",
        "date_returned",
        "late_fee",
      ],
    };
  },
  methods: {
    loadCopy() {
      const resp1 = this.$store.dispatch("library/fetchDetail", {
        type: "borrowed",
        id: this.id,
      });
      const resp2 = this.$store.dispatch("library/fetchHeaders", {
        type: "borrowed",
        id: this.id,
      });
      Promise.all([resp1, resp2]).then(() => {
        this.loading = false;
      });
    },
    async returnCopy() {
      await this.$store.dispatch("library/returnCopy", { book: this.id });
      this.dialog = false;
    },
    loadOpen() {
      this.loadCopy();
      this.dialog = true;
    },
  },
};
</script>

<style>
</style>