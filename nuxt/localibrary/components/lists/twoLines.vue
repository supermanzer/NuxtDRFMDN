<template>
  <v-list-item two-line>
    <v-list-item-content>
      <v-list-item-title>
        <slot name="title"></slot>
      </v-list-item-title>
      <v-list-item-subtitle>
        <slot name="subtitle"></slot>
      </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {};
</script>

<style>
</style>