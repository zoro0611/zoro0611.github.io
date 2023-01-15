const app = Vue.createApp({
    data(){
        return{
            styleInput: '',
            isVisible: true,
            color:''
        }
    },
    methods:{
        ChangeVisible(){
            this.isVisible = !this.isVisible
        },
    },
    computed:{
        // GetMyClass(){
        //     if(this.styleInput == 'user1'){
        //         return {user1: true, visible: this.isVisible, hidden: !this.isVisible}
        //     }
        //     else if(this.styleInput == 'user2'){
        //         return {user2: true, visible: this.isVisible, hidden: !this.isVisible}
        //     }
        //     else{
        //         return {visible: this.isVisible, hidden: !this.isVisible}
        //     }
            
        // },
        paraClasses(){
            return {
                user1: this.styleInput === 'user1',
                user2: this.styleInput === 'user2',
                visible: this.isVisible,
                hidden: !this.isVisible
            }
        }
    }
})

app.mount('#assignment')