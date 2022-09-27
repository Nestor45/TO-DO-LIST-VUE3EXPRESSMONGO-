import { createRouter, createWebHistory } from "vue-router"

import Home from "./views/InfoTable.vue"
import Form from './components/Form.vue'

const routes = [
    { path: "/", component: Home },
    { path: "/form", component: Form }
]

const history = createWebHistory();

const router = createRouter({
    history,
    routes,
});

export default router;