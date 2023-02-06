<template>
    <li>
        <h2>{{ name }} {{ isFavorite ? '(Favorite)':'' }}</h2>
        <button @click="toggleFavorite">{{isFavorite? 'Not':'Is'}} Favorite</button>
        <button @click="toggleDetails">{{detailsAreVisible? 'Hide':'Show'}} Details</button>
        <ul v-if="detailsAreVisible">
            <li><strong>Phone:</strong>{{ phoneNumber }}</li>
            <li><strong>Email:</strong>{{ emailAddress }}</li>
        </ul>
    </li>
</template>
<script>
export default {
    // props: ['name','phoneNumber','emailAddress','isFavorite'],
    props: {
        id:{
            type: String,
            required: true,
        },
        name: {
            type: String,
            required: true
        },
        phoneNumber: {
            type:String,
            required:true,
        },
        emailAddress: {
            type:String,
            required:true,
        },
        isFavorite: {
            type:Boolean,
            required:false,
            default: false,
            validator: function(value){
                return value === true || value === false
            }
        },
    },
    emits:[
        'toggle-favorite'
    ],
    // emits:{
    //     'toggle-favorite': function(id){
    //         if(id){
    //             return true
    //         }else{
    //             console.warn('Id is missing')
    //             return false
    //         }
    //     }
    // },
    data() {
        return {
            detailsAreVisible: false,
            friend: {
                id: 'manuel',
                name: 'Manuel Lorenz',
                phone: '0123 45678 90',
                email: 'manuel@localhost.com'
            },
            // friendIsFavorite: this.isFavorite //不能改變父層的值，用一個變數取代
        }
    },
    methods:{
        toggleDetails(){
            this.detailsAreVisible = !this.detailsAreVisible
            
        },
        toggleFavorite(){
            // this.friendIsFavorite = !this.friendIsFavorite
            this.$emit('toggle-favorite', this.id); //從子層呼叫父層的eventListener參數(在template裏頭@toggle-favorite方法)
            
            // this.$emit('toggle-favorite'); 
        }
    }
}
</script>