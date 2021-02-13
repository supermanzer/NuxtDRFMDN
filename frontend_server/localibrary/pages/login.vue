<template>
  <div class="fhw mt-12">
    <v-card>
      <v-img
        src="https://images.pexels.com/photos/65650/garden-shed-latch-lock-building-65650.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
        gradient="to top right, rgba(0,0,0, 0.7), rgba(0,0,0,0)"
        class="white--text align-end"
      >
        <v-card-title class="text-h3 px-6">Log In</v-card-title>
      </v-img>

      <v-divider></v-divider>
      <v-card-subtitle class="px-6"
        >To check out books, review your holds, and update your
        information</v-card-subtitle
      >
      <v-card-text class="pa-12">
        <v-row role="form">
          <v-col cols="12" sm="12" md="6">
            <v-text-field
              v-model="user.username"
              username
              label="User name"
              :rules="[rules.required]"
              prepend-inner-icon="mdi-account"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="6">
            <v-text-field
              v-model="user.password"
              type="password"
              label="password"
              :rules="[rules.required]"
              prepend-inner-icon="mdi-form-textbox-password"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions class="pa-12">
        <v-row>
          <v-col justify-center cols="12" sm="12">
            <v-btn color="primary" @click="login"> Log In </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
      rules: {
        required: (value) => !!value || "Required",
      },
    };
  },
  methods: {
    login() {
      this.$auth
        .login({ data: this.user })
        .then(() => this.$toast.success("Logged In"))
        .catch((e) => {
          console.log(e);
          this.$toast.error("Login failed", {
            duration: 1000,
            theme: "outline",
          });
        });
    },
  },
};
</script>

<style scoped>
div.fhw {
  width: 100%;
  height: 100%;
}
</style>