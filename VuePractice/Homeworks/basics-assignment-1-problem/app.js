const app = Vue.createApp({
    data() {
        return {
            myName: 'leo_hsu',
            myAge: 32,
            url: 'https://uploadfile.bizhizu.cn/up/67/42/95/674295674de1f1d6063a8a32339f89ce.jpg'
        }
    },
    methods: {
        getRdnNum(){
            var num = Math.random();
            return num;
        },
        getMyName(){
            return this.myName;
        }
    }
});
app.mount('#assignment');