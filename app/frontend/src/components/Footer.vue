<template>
    <footer class="footer-wrapper">
        <ul>
            <h3>Kontakt</h3>
            <li>E-mail 📧 | rezmak.k@gmail.com</li>
            <li>Discord 🎤 | Kacperek#8584</li>
        </ul>

        <ul>
            <h3>Menu</h3>
            <li> <router-link to="/">Analiza 📈</router-link> </li>
            <li> <router-link to="/about">Dane 💾</router-link> </li>
        </ul>

        <ul>
            <h3>Techniczne</h3>
            <li>API 🌐</li>
            <li>Dokumentacja 📕</li>
        </ul>

        <ul>
            <h3>Inne</h3>
            <li>O projekcie 📋</li>
            <li>Metodyka 🧪 </li>
        </ul>
    </footer>
</template>

<script>
export default {
    name: 'Footer',
    props: {
        msg: String,
    },
};
</script>

<style scoped>
.footer-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 100%;
    min-height: 54px;
    background-color: #E7E7E7;
    text-align: center;
    border-top: rgba(0, 0, 0, 0.25) solid 1px;
}

ul {
    list-style-type: none;
    padding: 0 0 1rem 0;
    margin: 0;
}

h3 {
    margin: 0.5rem;
}

a {
    color: #000;
}
</style>