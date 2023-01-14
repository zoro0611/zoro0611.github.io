const app = Vue.createApp({
    data(){
        return {
            alertMsg: 'no man',
            keydownVal:'',
            confirmValue:'',
        }
    },
    methods:{
        showAlert(){
            alert(`MSG: ${this.alertMsg}`)
        },
        showKeyDownVal(event){
            this.keydownVal = event.target.value
        },
        confirmVal(event){
            this.confirmValue = this.keydownVal
        }
    }


})

app.mount('#assignment')