<template>
  <div>
    <v-data-table
      :items="records"
      :headers="headers"
      hide-default-footer
      class="eleveation-1"
      :options.sync="options"
      :items-per-page="itemsPerPage"
      :page.sync="options.page"
    >
      <template v-slot:top>
        <slot name="table-top"></slot>
      </template>
      <!-- Figure out a way to to this from the page using this component with slots! -->
      <template v-slot:item.title="{ item }">
        <v-btn
          color="primary"
          text
          nuxt
          :to="{ name: 'books-id', params: { id: item.id } }"
          >{{ item.title }}</v-btn
        >
        <!-- <v-btn
          icon
          text
          color="primary"
          nuxt
          :to="{ name: 'books-id', params: { id: item.id } }"
        >
          <v-icon>mdi-magnify</v-icon>
        </v-btn> -->
      </template>
    </v-data-table>
    <v-pagination v-model="options.page" :length="pageCount"> </v-pagination>
  </div>
</template>

<script>
export default {
  name: "ExternalDataTable",
  props: {
    headers: { type: Array, required: true },
    records: { type: Array, required: true },
    pageCount: { type: Number, required: true },
  },
  computed: {
    itemsPerPage() {
      return this.records.length;
    },
  },
  data() {
    return {
      page: 1,
      options: {},
    };
  },
  watch: {
    options: {
      handler() {
        // console.log(this.options);
        this.$emit("table-change", this.options);
      },
      deep: true,
    },
    page: {
      handler() {
        this.$emit("page-change", this.options);
      },
      deep: true,
    },
  },
};
</script>

<style>
</style>