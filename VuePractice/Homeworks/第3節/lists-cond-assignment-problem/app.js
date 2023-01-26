const app = Vue.createApp({
    data(){
        return{
            tasks:[],
            input:'',
            showTxt: true
        }
    },
    methods:{
        addTask(){
            this.tasks.push(this.input)
            this.input = ''
        },
        changeShow(){
            this.showTxt = !this.showTxt
        }
    },

})
app.mount('#assignment')