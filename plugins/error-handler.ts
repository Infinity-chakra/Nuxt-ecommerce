export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.config.errorHandler = (error, instance, info) => {
      // handle error, e.g. report to a service
      console.log('Error: Nuxt', error)
    }
  
    // Also possible
    nuxtApp.hook('vue:error', (error, instance, info) => {
      // handle error, e.g. report to a service
      console.log('Error: Nuxt 2', error)
    })
  })
  