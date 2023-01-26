function getRandomValue(min, max){
    return Math.floor( Math.random() * (max - min) ) + min
}

const app = Vue.createApp({
    data(){
        return {
            playerHealth:100,
            monsterHealth:100,
            currentRound: 0,
            winner: null,
            logMsgArr: []
        }
    },
    methods:{
        startGame(){
            this.playerHealth = 100
            this.monsterHealth = 100
            this.currentRound = 0
            this.winner = null
            this.logMsgArr= []
        },
        atkMonster(){
            this.currentRound++
            const atkVal = getRandomValue(5,12)
            this.monsterHealth -= atkVal
            this.addLogMsg('player','attack',atkVal)

            this.atkPlayer()
            
        },
        atkPlayer(){
            const atkVal = getRandomValue(8,15)
            this.playerHealth -= atkVal
            this.addLogMsg('monster','attack',atkVal)

        },
        specialAtkMonster(){
            this.currentRound++
            const atkVal = getRandomValue(10,25)
            this.monsterHealth -= atkVal
            this.addLogMsg('player','attack',atkVal)
            this.atkPlayer()
        },
        healPlayer(){
            this.currentRound++
            const healVal = getRandomValue(8,20)
            if(this.playerHealth + healVal > 100){
                this.playerHealth = 100
            }
            else{
                this.playerHealth += healVal
            }
            this.addLogMsg('player','heal',healVal)
            this.atkPlayer()
        },
        surrender(){
            this.winner = 'monster'
        },
        addLogMsg(who, what, value){
            let obj = {
                actionBy: who,
                actionType: what,
                actionValue: value
            }
            this.logMsgArr.unshift(obj)
        }
    },
    computed:{
        monsterBarStyles(){
            if(this.monsterHealth <0){
                return {width: '0%'}
            }
            return {width: this.monsterHealth + '%'}
        },
        playerBarStyles(){
            if(this.playerHealth <0){
                return {width: '0%'}
            }
            return {width: this.playerHealth + '%'}
        },
        mayUseSpecialAtk(){
            return this.currentRound % 3 != 0
        }
    },
    watch:{
        playerHealth(value){
            if(value <=0 && this.monsterHealth <=0){
                this.winner = 'draw'
            }
            else if(value <=0){
                this.winner = 'monster'
            }
        },
        monsterHealth(value){
            if(value<=0 && this.playerHealth <=0){
                this.winner = 'draw'
            }
            else if(value<=0){
                this.winner = 'player'
            }
        },
    },
    mounted(){
        // console.log('hello world')
    }
})
app.mount('#game')