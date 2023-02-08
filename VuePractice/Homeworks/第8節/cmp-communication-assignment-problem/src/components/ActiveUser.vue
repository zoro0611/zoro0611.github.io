<template>
    <div>
        <ul>
            <li>
                <h2>{{name}}</h2>
                <h3>{{age}}</h3>
            </li>
        </ul>
    </div>
</template>
<script>
    export default{
        props:{
            name:{
                type: String,
                required: true,
            },
            age: {
                type: String,
                required: true
            },
        },
        data(){
            return{

            }
        },
    }
</script>
<style>
    li{
        list-style: none;
    }
</style>