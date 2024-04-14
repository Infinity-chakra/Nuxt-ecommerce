// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css'
import '../themes/dark'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'

const myCustomTheme = {
  colors: {
    primary: '#ff0011',
    accent: '#ffc107',
    success: '#28a745',
  },
};

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    // ... your configuration
    theme: myCustomTheme,
  })
  app.vueApp.use(vuetify)
})