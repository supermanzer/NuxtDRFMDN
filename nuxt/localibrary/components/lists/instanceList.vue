<template>
  <v-list three-line>
    <template v-for="instance in instances">
      <v-list-item :key="instance.id">
        <v-list-item-icon>
          <v-icon>mdi-book</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title :class="getClass(instance)">
            {{ instance.inst_status }}
          </v-list-item-title>
          <v-list-item-subtitle v-if="instance.due_date">
            <span class="fot-weight-bold">Due Back:</span>
            {{ instance.due_date }}
          </v-list-item-subtitle>
          <v-list-item-subtitle>
            <span class="mr-4">Publisher: {{ instance.imprint }}</span>
            <span class="ml-4">ID: {{ instance.id }}</span>
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>
  </v-list>
</template>

<script>
export default {
  name: "InstanceList",
  props: {
    instances: { type: Array, required: true },
  },
  methods: {
    getClass(inst) {
      const colors = {
        a: "green--text",
        o: "amber--text",
        r: "red--text",
        m: "red--text text--darken-4",
      };
      return colors[inst.status];
    },
  },
};
</script>

<style>
</style>