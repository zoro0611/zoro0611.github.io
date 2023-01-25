const app = Vue.createApp({
    data() {
        return {
            courseGoalA: 'Finish the course and learn Vue!',
            courseGoalB: '<h3>Master Vue and build amazing apps!</h3>',
            vueLink: 'https://vuejs.org/'
        };
    },
    methods: {
        // changeTxt() {
        //     this.courseGoal = 'I just changed Text!!'
        // },
        outputGoal(){
            const randomNumber = Math.random();
            if(randomNumber < 0.5){
                return this.courseGoalA;
            }
            else{
                return this.courseGoalB;
            }
        }
    }
});



app.mount('#user-goal');

