const app = Vue.createApp({
    data(){
        return{
            totalValue: 0,
            reminder:''
        }
    },
    methods:{
        Add(num){
            this.totalValue += num
        },
        Reset(){
            this.totalValue = 0
        }
    },
    computed:{
        Result(){
            console.log(this.totalValue)
            if(this.totalValue > 37){
                return 'Too much!'
            }
            else if(this.totalValue == 37){
                return this.totalValue
            }
            else{
                return 'Not there yet!'
            }
        }
    },
    watch:{
        Result(value){
            console.log('watcher works')
            const that = this
            setTimeout(function(){
                that.totalValue = 0
            },5000)
        }
    }


})

app.mount('#assignment')