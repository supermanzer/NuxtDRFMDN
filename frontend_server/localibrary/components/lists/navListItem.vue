<template>
  <v-list-item :to="item.to" router exact class="py-4">
    <v-list-item-action>
      <v-icon>{{ item.icon }}</v-icon>
    </v-list-item-action>
    <v-list-item-content>
      <v-list-item-title v-text="item.title" />
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  name: "NavListItem",
  props: {
    item: { type: Object, required: true },
    i: { type: Number, required: true },
  },
};
</script>

<style>
</style>