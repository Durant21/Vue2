<template>
        <div>
          <input type="text" v-model="message">
          <p>1  {{ message }}</p>
        </div>
</template>

<script>
    export default {
      data() {
          return {
            message: ''
          }
      }
    }
</script>

<style>

</style>
