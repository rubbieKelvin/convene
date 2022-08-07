<template>
  <div>
    <label for="">Email</label>
    <input v-model="form.email" type="text" placeholder="email" /><br />
    <label for="">Password</label>
    <input v-model="form.password" type="password" placeholder="password" /><br />
    <input type="submit" value="Submit"/>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const form = ref({
      email: "",
      password: "",
    });

    return { form };
  },
});
</script>
