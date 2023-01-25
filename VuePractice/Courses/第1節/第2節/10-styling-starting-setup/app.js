const app = Vue.createApp({
    data(){
        return{
            boxASelected: false,
            boxBSelected: false,
            boxCSelected: false,
        }
    },
    methods:{
        boxSelected(box){
            if (box === 'A'){
                this.boxASelected = true
            }
            else if (box === 'B'){
                this.boxBSelected = true
            }
            else if (box === 'C'){
                this.boxCSelected = true
            }
        }
    },
    computed:{
        boxAClasses(){
            return {demo: true ,active:this.boxASelected}
        },
        boxBClasses(){
            return {demo: true ,active:this.boxBSelected}
        },
        boxCClasses(){
            return {demo: true ,active:this.boxCSelected}
        }
    }
})

app.mount('#styling')