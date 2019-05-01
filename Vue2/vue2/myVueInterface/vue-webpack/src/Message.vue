<template>
  <div>
    <h1>this is a great message!!</h1>
    <app-input></app-input>
  </div>
</template>


<script>
  import Input from './Input.vue';

  export default {
    components: {
      'app-input': Input
    }
  }
</script>
