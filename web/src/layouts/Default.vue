<template>
    <div>
        <NavBar/>
        <div>
            <slot/>
        </div>
    </div>
</template>

<script>
import NavBar from '@/components/NavBar'
export default {
    components:{
        NavBar
    }
}
</script>
