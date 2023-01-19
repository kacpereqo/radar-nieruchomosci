<template>
    <div>
        <form action="#" method="get">
            <div class="form-group">
                <div>
                    <label for="Województwo">Województwo </label>
                    <select name="region" id="region">
                        <option value="" disabled selected>Select your option</option>
                        <option value="1">Małopolskie</option>
                        <option value="2">dolnośląskie</option>
                        <option value="3">kujawsko-pomorskie</option>
                        <option value="4">lubelskie</option>
                        <option value="5">lubuskie</option>
                        <options value="6">łódzkie</options>
                        <option value="7">mazowieckie</option>
                        <option value="8">opolskie</option>
                        <option value="9">podkarpackie</option>
                        <option value="10">podlaskie</option>
                        <option value="11">pomorskie</option>
                        <option value="12">śląskie</option>
                        <option value="13">świętokrzyskie</option>
                        <option value="14">warmińsko-mazurskie</option>
                        <option value="15">wielkopolskie</option>
                        <option value="16">zachodniopomorskie</option>
                    </select>
                </div>

                <div>

                </div>
            </div>
        </form>
        <div class="chart-wrapper">
            <form action="#" method="get">
                <div class="chart-form">
                    <button type="button">1D</button>
                    <button type="button">1T</button>
                    <button type="button">1M</button>
                    <button type="button">3M</button>
                    <button type="button">6M</button>
                    <button type="button">1Y</button>
                    <button type="button">5Y</button>
                    <button type="button">MAX</button>
                    <button type="button">Ustaw własny</button>
                </div>
            </form>
            <UplotVue :options="options" :data="data" />
        </div>
    </div>
</template>


<script>
import UplotVue from "uplot-vue";


export default {
    name: "Chart",
    components: { UplotVue, Autocomplete },
    data() {
        return {
            city: "",
            options: {

                width: 900,
                height: 400,
                series: [
                    {
                        label: "Data",
                    },
                    {
                        label: "",
                        points: { show: false },
                        stroke: "#00437a",
                        fill: "#00437a22",
                    },

                ],
                axes: [
                    {
                        label: "Data",

                    },
                    {
                        label: "Cena [PLN]",

                    },

                ],
                scales: { x: { time: false } },
            },
        };
    },
    beforeMount() {
        this.data = [
            [...new Array(1000)].map((_, i) => i),
            [...new Array(1000)].map((_, i) => i % 1000),
        ];
    },
    mounted() {
        setInterval(() => {
            const options = {
                ...this.options,
            };
            const data = [
                [...this.data[0], this.data[0].length],
                [...this.data[1], this.data[0].length % 1000],
            ];
            this.data = data;
            this.options = options;
        }, 1000);
    },
    methods: {
        autocomplete() {
            console.log(this.city);
        },
    },
};



</script>

<style scoped>
.chart-wrapper {
    border: rgba(0, 0, 0, 0.25) solid 1px;
}

.chart-form {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.chart-form button {
    margin: 10px;
    border: rgba(0, 0, 0, 0.25) solid 1px;
    border-radius: 3px;
    background-color: #fff;
}

.chart-form button:hover {
    background-color: #dddddd;
    cursor: pointer;
}

.form-group {
    display: grid;
    grid-template-columns: 2w 2;
    margin: 10px;
    border: rgba(0, 0, 0, 0.25) solid 1px;
    min-width: clamp(200px, 50vw, 800px);
    min-height: 200px;
}
</style>
