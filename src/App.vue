<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import QuestionView from './components/Question.vue'
import HomeView from './components/Home.vue'
import AccountView from './components/Account.vue'

import { Auth } from 'aws-amplify'
import { CognitoHostedUIIdentityProvider } from '@aws-amplify/auth'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

async function login() {
  Auth.federatedSignIn({ provider: CognitoHostedUIIdentityProvider.Google })
}

onMounted(async () => {
  try{
    const currentUser = await Auth.currentAuthenticatedUser()
    console.log(currentUser)
  }
  catch{
    router.push({ name: 'login'})
    console.log("no user")
  }
})
</script>

<template>
  <router-view :key="$route.path"></router-view>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
