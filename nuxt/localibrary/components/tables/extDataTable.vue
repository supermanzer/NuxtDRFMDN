<template>
  <div>
    <v-data-table
      :items="records"
      :headers="headers"
      hide-default-footer
      class="elevation-1"
      :options.sync="options"
      :items-per-page="itemsPerPage"
      :page.sync="options.page"
    >
      <template v-slot:top>
        <slot name="table-top"></slot>
      </template>
      <template v-slot:item.summary="{ item }">
        {{ item.summary | truncate }}
      </template>
      <template v-slot:item.actions="{ item }">
        <slot name="table-actions" v-bind:item="item">
          <v-icon>mdi-magnify</v-icon>
        </slot>
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
  filters: {
    truncate: function (text) {
      if (text !== undefined) {
        const charLength = 120; // Set number of characters to display
        if (text.length > charLength) {
          return text.substring(0, charLength) + "...";
        }
        return text;
      }
    },
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