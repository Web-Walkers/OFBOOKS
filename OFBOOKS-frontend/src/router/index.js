import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  scrollBehavior(to, from, savedPosition) {
    return { top: 0, behavior: 'smooth'}
  },
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/AboutView.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/RegisterView.vue'),
    },
    {
      path: '/blogs/:id',
      name: 'blogs',
      component: () => import('@/views/BlogsView.vue'),
    },
    {
      path: '/products',
      name: 'products',
      component: () => import('@/views/ProductsView.vue'),
    },
    {
      path: '/reading',
      name: 'reading',
      component: () => import('@/views/ReadingView.vue'),
    },
    {
      path: '/shipping/:id',
      name: 'shipping',
      component: () => import('@/views/ShippingView.vue'),
    },
    {
      path: '/my-cart',
      name: 'my-cart',
      component: () => import('@/views/MyCartView.vue'),
    },
    {
      path: '/Payment/:id',
      name: 'payment',
      component: () => import('@/views/PaymentView.vue'),
    },
    {
      path: '/done/:id',
      name: 'done',
      component: () => import('@/views/DoneView.vue'),
    },
    {
      path: '/blog/:id',
      name: 'blog',
      component: () => import('@/views/BlogView.vue'),
    },
    {
      path: '/product/:id',
      name: 'product',
      component: () => import('@/views/ProductView.vue'),
    },
    {
      path: '/book/:id',
      name: 'book',
      component: () => import('@/views/BookView.vue'),
    },
    {
      path: '/startreading',
      name: 'startreading',
      component: () => import('@/views/StartReadingView.vue'),
    },
    // --- Profile ---
    {
      path: '/profile/:id',
      component: () => import('@/views/ProfileView.vue'),
      children: [
        {
          path: '',
          name: 'profile',
          component: () => import('@/views/profile/ProfileView.vue'),
        },
        {
          path: 'my-libery',
          name: 'my-libery',
          component: () => import('@/views/profile/MyLiberyView.vue'),
        },
        {
          path: 'my-shopping',
          name: 'my-shopping',
          component: () => import('@/views/profile/MyShoppingView.vue'),
        },
        {
          path: 'my-address',
          name: 'my-address',
          component: () => import('@/views/profile/MyAddressView.vue'),
        },
        {
          path: 'my-messages',
          name: 'my-messages',
          component: () => import('@/views/profile/MyMessagesView.vue'),
        },
        {
          path: 'my-reading',
          name: 'my-reading',
          component: () => import('@/views/profile/MyReadingView.vue'),
        },
        {
          path: 'my-blogs',
          name: 'my-blogs',
          component: () => import('@/views/profile/MyBlogsView.vue'),
        },
        {
          path: 'my-wallet',
          name: 'my-wallet',
          component: () => import('@/views/profile/MyWalletView.vue'),
        },
        {
          path: 'request-book',
          name: 'request-book',
          component: () => import('@/views/profile/RequestBookView.vue'),
        },
        {
          path: 'affiliate-marketing',
          name: 'affiliate-marketing',
          component: () => import('@/views/profile/AffiliateMarketingView.vue'),
        },
      ],
    },
    // Search Book
    {
      path: '/subject/:id',
      name: 'subject',
      component: () => import('@/views/SubjectView.vue'),
    },
    {
      path: '/publisher/:id',
      name: 'publisher',
      component: () => import('@/views/PublisherView.vue'),
    },
    {
      path: '/literature/:id',
      name: 'literature',
      component: () => import('@/views/LiteratureView.vue'),
    },
    // Error404
    { path: '/:pathMatch(.*)*', name: 'Page Not Found', component: () => import('@/views/PageNotFoundView.vue')},
  ]
})

export default router
