<template>
  <div>
    <!-- <the-header></the-header> -->
    <TheHeader />
    <!-- <BadgeList />
    <user-info
      :full-name="activeUser.name"
      :info-text="activeUser.description"
      :role="activeUser.role"
    ></user-info>
    <course-goals>
      <template #default="slotProps">
        <h2>{{ slotProps.item }}</h2>
        <p>{{ slotProps['anotherProp'] }}</p>
      </template>
    </course-goals> -->
    <button @click="setSelectedComponents('active-goals')">Active Goals</button>
    <button @click="setSelectedComponents('manage-goals')">Manage Goals</button>
    <!-- <ActiveGoals v-if="this.selectedComponents === 'active-goals'"/>
    <ManageGoals v-if="this.selectedComponents === 'manage-goals'"/> -->
    <component :is="selectedComponents"></component>
  </div>
</template>

<script>
import TheHeader from './components/TheHeader.vue'
// import BadgeList from './components/BadgeList.vue'
// import UserInfo from './components/UserInfo.vue'
// import CourseGoals from './components/CourseGoals.vue'
import ActiveGoals from './components/ActiveGoals.vue'
import ManageGoals from './components/ManageGoals.vue'

export default {
  components:{
    // 'the-header': TheHeader
    TheHeader,
    // BadgeList,
    // // 'user-info': UserInfo,
    // UserInfo,
    // CourseGoals,
    ActiveGoals,
    ManageGoals,
  },
  data() {
    return {
      selectedComponents:'active-goals',
      activeUser: {
        name: 'Maximilian Schwarzmüller',
        description: 'Site owner and admin',
        role: 'admin',
      },
    };
  },
  methods:{
    setSelectedComponents(cmp){
      this.selectedComponents = cmp
    }
  }
};
</script>

<style>
html {
  font-family: sans-serif;
}

body {
  margin: 0;
}
</style>