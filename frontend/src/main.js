import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import call from './data/call.js'

import {
  Button,
  Card,
  Input,
  setConfig,
  frappeRequest,
  resourcesPlugin,
} from 'frappe-ui'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)

app.component('Button', Button)
app.component('Card', Card)
app.component('Input', Input)
app.provide('call', call)

app.mount('#app')
