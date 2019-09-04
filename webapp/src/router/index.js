import Vue from 'vue'
import Router from 'vue-router'
import login from '../views/login.vue'
import loginIn from '../views/loginIn.vue'
import homepage from '../components/TheHomePage.vue'
import userpage from '../components/TheUserPage.vue'
import netpage from '../components/TheNetPage.vue'
import statepage from '../components/TheStatePage.vue'
import mappage from '../components/TheMapPage.vue'
import TheGameCanvas from '../components/TheGameCanvas'

Vue.use(Router);
const routerPush = Router.prototype.push;
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error=> error)
};

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/in',
      name: 'in',
      component: loginIn,
      children: [
        {
          path: 'homepage',
          name: 'homepage',
          component: homepage
        },
        {
          path: 'userpage',
          name: 'userpage',
          component: userpage
        },
        {
          path: 'netpage',
          name: 'netpage',
          component: netpage
        },
        {
          path: 'statepage',
          name: 'statepage',
          component: statepage
        },
        // {
        //   path: 'mappage',
        //   name: 'mappage',
        //   component: mappage
        // },
      ]
    }
  ]
})
