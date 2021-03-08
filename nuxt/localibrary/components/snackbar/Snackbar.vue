<!-- 
    components/snackbar/Snackbar.vue

    Defines a basic snackbar component that uses state values to populate
-->
<template>
  <v-snackbar
    v-model="show"
    top
    app
    :timeout="timeout"
    :color="color"
    :text="false"
  >
    {{ text }}

    <template v-slot:action="{ attrs }">
      <v-btn color="deep-purple" text v-bind="attrs" @click="show = false">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  name: "Snackbar",
  data() {
    return {
      show: false,
      timeout: 4000,
      text: "",
    };
  },
  created() {
    this.$store.watch(
      (state) => state.snack.text,
      () => {
        const msg = this.$store.state.snack.text;
        if (msg !== "") {
          this.text = msg;
          this.show = true;
          this.$store.commit("snack/SET_SNACK", { text: "" });
        }
      }
    );
  },
  computed: {
    color() {
      return this.$store.state.snack.color;
    },
  },
};
</script>

<style>
</style>