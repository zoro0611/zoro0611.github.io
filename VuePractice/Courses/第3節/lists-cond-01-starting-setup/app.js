const app = Vue.createApp({
  data() {
    return {
      goals: [
        
      ],
      enterGoalValue:'',

    }
  },
  methods:{
    addGoal(){
      this.goals.push(this.enterGoalValue);
    }
  }
})

app.mount('#user-goals')
