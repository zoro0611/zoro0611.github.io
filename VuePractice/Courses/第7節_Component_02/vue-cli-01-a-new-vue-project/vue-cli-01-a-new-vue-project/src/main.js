import {createApp} from 'vue';

import App from './App.vue';
import FrienedContact from './components/FriendContact.vue';

const app = createApp(App)

app.component('friend-contact', FrienedContact);

app.mount('#app')