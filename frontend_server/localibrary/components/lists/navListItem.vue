<template>
  <v-tooltip v-if="mini" right>
    <template v-slot:activator="{ on, attrs }">
      <v-list-item
        :to="item.to"
        router
        exact
        class="py-4"
        v-bind="attrs"
        v-on="on"
      >
        <v-list-item-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title v-text="item.title" />
        </v-list-item-content>
      </v-list-item>
    </template>
    <span v-text="item.title"></span>
  </v-tooltip>
  <div v-else>
    <v-list-item :to="item.to" router exact class="py-4">
      <v-list-item-action>
        <v-icon>{{ item.icon }}</v-icon>
      </v-list-item-action>
      <v-list-item-content>
        <v-list-item-title v-text="item.title" />
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
export default {
  name: "NavListItem",
  props: {
    item: { type: Object, required: true },
    i: { type: Number, required: true },
    mini: { type: Boolean, required: false, default: false },
  },
};
</script>

<style>
</style>