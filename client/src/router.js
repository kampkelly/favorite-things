import Vue from 'vue';
import Router from 'vue-router';
import store from './store.js'
import Home from './views/Home.vue';
import Signup from './components/Signup.vue';
import Signin from './components/Signin.vue';
import Registration from './views/Registration.vue';
import AddFavorite from './views/Favorites/createFavorite.vue';
import AllFavorites from './components/allFavorites.vue';
import CategoryFavorites from './components/categoryFavorites.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { 
        requiresAuth: true
      },
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration,
      children: [
        {
          path: '',
          component: Signup,
        },
        {
          path: 'signup',
          component: Signup,
        },
        {
          path: 'signin',
          component: Signin,
        },
      ],
      meta: { 
        requiresNoAuth: true
      },
    },
    {
      path: '/favorites',
      name: 'favorites',
      component: Home,
      children: [
        {
          path: '',
          component: AllFavorites,
        },
        {
          path: 'all',
          component: AllFavorites,
        },
        {
          path: 'category',
          component: CategoryFavorites,
        },
      ],
      meta: { 
        requiresAuth: true
      },
    },
    {
      path: '/add-favorite',
      name: 'addFavorite',
      component: AddFavorite,
      meta: { 
        requiresAuth: true
      },
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
  ],
});

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return
    }
    next('/registration/signin') 
  } else if (to.matched.some(record => record.meta.requiresNoAuth)) {
    if (!store.getters.isAuthenticated) {
      next();
      return
    }
    next('/');
  } else {
    next() ;
  }
});

export default router;
