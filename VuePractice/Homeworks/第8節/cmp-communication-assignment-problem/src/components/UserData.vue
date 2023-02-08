<template>
    <form @submit.prevent="SubmitData">
        <div>
            <label for="">Name</label>
            <input type="text" v-model="enteredName">
        </div>
        <div>
            <label for="">Age</label>
            <input type="text" v-model="enteredAge">
        </div>
        <button>Add User</button>
    </form>
</template>
<script>
    export default{
        emits:[
            'add-user'
        ],
        data(){
            return{
                enteredName:'',
                enteredAge:'',

            }
        },
        methods:{
            SubmitData(){
                this.$emit('add-user',
                    this.enteredName,
                    this.enteredAge
                
                )
            }
        }
    }
</script>