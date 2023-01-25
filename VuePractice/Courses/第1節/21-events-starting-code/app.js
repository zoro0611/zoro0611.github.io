const app = Vue.createApp({
  data() {
    return {
      counter: 10,
      name: '',
      confirmName:''
    };
  },
  methods:{
    addCounter(num){
      this.counter += num
    },
    reduceCounter(num){
      this.counter-=num
    },
    setName(event,lastname){
      this.name = event.target.value + ' ' + lastname; 
    },
    submitForm(event){
      // event.preventDefault();
      alert('Submitted!')
    },
    confirmInput(){
      this.confirmName = this.name;
    }
  }
});

app.mount('#events');
