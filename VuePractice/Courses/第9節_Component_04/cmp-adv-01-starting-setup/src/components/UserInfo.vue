<template>
  <section>
    <base-card>
      <template #header>
        <h3>{{ fullName }}</h3>
        <base-badge :type="role" :caption="role.toUpperCase()"></base-badge>
      </template>
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
