<template>
  <section>
    <base-card>
      <header>
        <h3>{{ fullName }}</h3>
        <base-badge :type="role" :caption="role.toUpperCase()"></base-badge>
      </header>
      <p>{{ infoText }}</p>
    </base-card>
  </section>
</template>

<script>
// import BaseBadge from './BaseBadge.vue'
export default {
  components:{
    // 'base-badge': BaseBadge,
  },
  props: ['fullName', 'infoText', 'role'],
};
</script>

<style scoped>


section header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>