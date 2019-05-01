import Vue from 'vue';
import App from './App.vue';
import Message from './Message.vue';

Vue.component('app-message', Message);   //this will be the HTML tag name called in the App.vue file.

new Vue({
  el: '#app',
  render: h => h(App)
});
