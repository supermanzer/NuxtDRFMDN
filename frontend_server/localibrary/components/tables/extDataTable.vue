<template>
  <div>
    <v-data-table
      :items="records"
      :headers="headers"
      hide-default-footer
      class="eleveation-1"
      :page.sync="page"
      :items-per-page="itemsPerPage"
    >
    </v-data-table>
    <v-pagination v-model="page" :length="pageCount"> </v-pagination>
  </div>
</template>

<script>
export default {
  name: "ExternalDataTable",
  props: {
    headers: { type: Array, required: true },
    records: { type: Array, required: true },
    page: { type: Number, required: true },
    pageCount: { type: Number, required: true },
  },
  computed: {
    itemsPerPage() {
      return this.records.length;
    },
  },
  data() {
    return {
      loading: true,
    };
  },
};
</script>

<style>
</style>