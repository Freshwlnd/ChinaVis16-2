import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/homepage',
    },
    {
      path: '/homepage',
      component: resolve => require(['../components/common/Menu.vue'], resolve),
      children:[
        {
          path: '/homepage',
          component: resolve => require(['../components/homepage.vue'], resolve)
        },
        {
          path: '/CircularScatter',
          component: resolve => require(['../components/CircularScatter.vue'], resolve)
        },
        {
          path: '/Sunburst',
          component: resolve => require(['../components/Sunburst.vue'], resolve)
        },
        {
          path: '/Cloud',
          component: resolve => require(['../components/Cloud.vue'], resolve)
        },
        {
          path: '/Matrix',
          component: resolve => require(['../components/Matrix.vue'], resolve)
        },
        {
          path: '/line',
          component: resolve => require(['../components/line.vue'], resolve)
        }
      ]
    }
  ]
})
