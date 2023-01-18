<template>
    <div>
        <UplotVue :options="options" :data="data" />
    </div>
</template>

<script>
import "uplot/dist/uPlot.min.css";

import UplotVue from "uplot-vue";

export default {
    name: "Chart",
    components: { UplotVue },
    data() {
        return {
            options: {
                title: "Test",
                width: 500,
                height: 300,
                series: [
                    {
                        label: "Date",
                    },
                    {
                        label: "",
                        points: { show: false },
                        stroke: "#00437a",
                        fill: "#00437a22",
                    },
                ],
                scales: { x: { time: false } },
            },
        };
    },
    beforeMount() {
        // Initialize data inside mounted hook, to prevent Vue from adding watchers, otherwise performance becomes unbearable
        this.data = [
            [...new Array(1000)].map((_, i) => i),
            [...new Array(1000)].map((_, i) => i % 1000),
        ];
    },
    mounted() {
        setInterval(() => {
            const options = {
                ...this.options,
                title: "Wykres czasu od czasu",
            };
            const data = [
                [...this.data[0], this.data[0].length],
                [...this.data[1], this.data[0].length % 1000],
            ];
            this.data = data;
            // Since we disabled reactivity for data above
            // ???
            //this.$forceUpdate();
            this.options = options;
        }, 1000);
    },
};
</script>

<style scoped>

</style>
