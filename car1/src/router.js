import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      components: {
        default: () => import('@/views/Index')
      },
    },
    {
      path: '/regsiter',
      name: 'regsiter',
      components: {
        default: () => import('@/views/regsiter')
      },
    },
    {
      path: '/Vehiclelist',
      name: 'Vehiclelist',
      components: {
        default: () => import('@/views/Vehiclelist')
      },
    },
    {
      path: '/Reportlist',
      name: 'Reportlist',
      components: {
        default: () => import('@/views/Reportlist')
      },
    },
    {
      path: '/user',
      name: 'user',
      components: {
        default: () => import('@/views/user')
      },
    },
    {
      path: '/manager',
      name: 'manager',
      components: {
        default: () => import('@/views/manager')
      },
    },
    {
      path: '/operators',
      name: 'operators',
      components: {
        default: () => import('@/views/operators')
      },
    },
    {
      path: '/pay',
      name: 'pay',
      components: {
        default: () => import('@/views/pay'),
      },
    },
    {
      path: '/my',
      name: 'my',
      components: {
        default: () => import('@/views/my'),
      },
    }
  ],
})
