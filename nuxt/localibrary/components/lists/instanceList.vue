<template>
<v-row>
  <v-col cols="12" sm="12">
      <span>{{ num_instances }} Copies, {{ num_available }} Available</span>
      <v-btn icon @click="showInstances = !showInstances">
        <v-icon>{{
          showInstances ? "mdi-chevron-up" : "mdi-chevron-down"}}
        </v-icon>
      </v-btn>
  </v-col>
  <v-col cols="12" sm="12">
    <v-expand-transition>
        <div v-show="showInstances" class="pa-4">
            <v-divider></v-divider>
            <h3 class="text-h5">Copies</h3>
            <v-list three-line>
              <template v-for="instance in instances">
                <instance-item @check-out="refreshInstances" :instance="instance" :key="instance.id"></instance-item>
              </template>
            </v-list>
         </div>
     </v-expand-transition>
  </v-col>
        
</v-row>

</template>

<script>
import instanceItem from "@/components/lists/instanceItem";

export default {
  components: { instanceItem },
  name: "InstanceList",
  props: {
    id: { type: Number, required: true }, // Book ID
  },
  data: () => ({
    instances: [],
    showInstances: false
  }),
  computed: {
    num_instances() {
      return this.instances.length
    },
    num_available() {
      return this.instances.filter(i => i.status === 'a').length
    }
  },
  async fetch() {
    const suffix = 'instances'
    const type = 'books'
    this.instances = await this.$store.dispatch('library/fetchAction', {type, id: this.id, suffix})
  },
  methods: {
    refreshInstances() {
      this.$fetch()
    }
  }
};
</script>

<style>
</style>