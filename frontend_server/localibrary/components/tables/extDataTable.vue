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