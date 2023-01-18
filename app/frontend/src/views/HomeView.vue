<template>
  <div class="wrapper">
    <Chart />
  </div>
</template>

<script>
import Chart from '@/components/Chart.vue';

export default {
  name: 'HomeView',
  components: {
    Chart,
  },
};

</script>


<style scoped>
.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>