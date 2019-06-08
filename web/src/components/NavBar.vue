<template>
    <div class="ui teal inverted clearing segment">
        <div class="ui grid">
            <div class="two wide column right floated middle aligned">
                <h3 class="ui header inverted">Hola {{user.nombres}}</h3>
            </div>
            <div class="two wide column">
                <input type="button" value="Cerrar sesión" class="ui button orange" @click="logout">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted(){
        this.user = this.$session.get('user')
    },
    methods:{
        logout(){
            this.$session.remove('user')
            this.$router.push('/')
        }
    },
    data(){
        return{
            user: {}
        }
    }
}
</script>
