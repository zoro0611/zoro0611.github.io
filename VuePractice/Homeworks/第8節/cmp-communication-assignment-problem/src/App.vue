<template>
    <user-data @add-user="AddUser">
    </user-data>
    <active-user
        v-for=" user in users"
        :key="user.userName"
        :name="user.userName"
        :age="user.userAge"
    ></active-user>
</template>

<script>
    export default{
        data(){
            return {
                users:[
                    {
                        userName:'Leo',
                        userAge:32
                    },
                    {
                        userName:'Megan',
                        userAge: 30
                    },

                ],
            }
        },
        methods:{
            AddUser(name, age){
                const user = {
                    userName: name,
                    userAge: age
                }
                this.users.push(user)
            }
        }
    }
</script>