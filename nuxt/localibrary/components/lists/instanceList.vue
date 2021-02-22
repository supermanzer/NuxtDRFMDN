<template>
  <v-list three-line>
    <template v-for="instance in instances">
      <instance-item :instance="instance" :key="instance.id"></instance-item>
    </template>
  </v-list>
</template>

<script>
import instanceItem from "@/components/lists/instanceItem";

export default {
  components: { instanceItem },
  name: "InstanceList",
  props: {
    instances: { type: Array, required: true },
  },
};
</script>

<style>
</style>