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
              v-on:keyup.enter="login"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="6">
            <v-text-field
              v-model="user.password"
              type="password"
              label="password"
              :rules="[rules.required]"
              prepend-inner-icon="mdi-form-textbox-password"
              v-on:keyup.enter="login"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row v-if="error">
          <v-col cols="12" sm="10" offset-sm="1">
            <v-alert
              type="error"
              text
              icon="mdi-alert-circle-outline"
              prominent
              elevation="2"
            >
              <p class="headline">Login Failure</p>
              <v-divider></v-divider>
              <p>
                This login attempt failed. Please check your username and
                password. If the problem persists, give up
              </p>
            </v-alert>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions class="pa-12">
        <v-row>
          <v-col cols="12" sm="12">
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="login"> Log In </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
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
      error: false,
    };
  },
  methods: {
    login() {
      this.$auth
        .login({ data: this.user })
        .then(() => {
          this.snackTime({
            text: "Login Successful",
            classname: "green--text",
          });
        })
        .catch((e) => {
          this.snackTime({ text: "Login Failed", classname: "red--text" });
          this.error = true;
          console.log(e);
        });
    },
    ...mapMutations({
      snackTime: "snack/SET_SNACK",
    }),
  },
};
</script>

<style scoped>
div.fhw {
  width: 100%;
  height: 100%;
}
</style>