<template>
    <nav class="nav-wrapper">
        <img src="@/assets/logo.png" alt="logo" class="logo" />
        <div class="links">
            <router-link to="/">Analiza 📈</router-link>
            <router-link to="/about">Dane 💾</router-link>
        </div>

    </nav>
</template>

<script>
export default {
    name: 'NavBar',
    props: {
        msg: String,
    },
};
</script>

<style scoped>
.nav-wrapper {
    min-height: 54px;
    display: flex;
    width: 100%;
    align-items: center;
    background-color: #e7e7e7;
    border-bottom: rgba(0, 0, 0, 0.25) solid 1px;
}

.logo {
    margin: 0 1rem;
    position: absolute;
    height: 50px;
    widows: 50px;

}

.links {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;
}

.links a {
    text-decoration: none;
    color: #000;
    font-size: 1.25rem;
    padding: 0 1rem;
    line-height: 54px;
}
</style>