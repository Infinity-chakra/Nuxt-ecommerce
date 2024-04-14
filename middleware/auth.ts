export default defineNuxtRouteMiddleware(async () => {
    const user = {
        username: 'Amit',
    }
    console.log('Auth middleware called', user.username)
    if (user.username === 'Amit') return navigateTo({name : 'items'});
    else return navigateTo({name : 'index'});
  });