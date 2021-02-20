<template>
  <p class="text--h1">Bye Bye</p>
</template>

<script>
export default {
  created() {
    this.$auth.logout();
  },
};
</script>

<style>
</style>