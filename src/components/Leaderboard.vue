<template>
  <div id="leaderboard-container">
    <div id="leaderboard">
      <h1 class="title">Leaderboard</h1>
      <p class="leaderboard-item" v-for="score in scores">
        {{ score.username }}: {{ score.score }}
      </p>
      <router-link class="button" to="/play"><button>Play again</button></router-link>
      <router-link class="button" to="/"><button>Back</button></router-link>
    </div>
    <div id="background-image-container">
      <div id="background-image"></div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, onMounted } from 'vue'
import { Auth } from 'aws-amplify'
const arr: any = []

let scores = reactive(arr)

var highScore = 0

onMounted(async () => {
  const user = await Auth.currentAuthenticatedUser()
  fetch('https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/leaderboard', {
    headers: {
      Authorization: 'Bearer ' + user.signInUserSession.accessToken.jwtToken
    }
  }).then((res) => {
    res.json().then((data) => {
      let count = 0
      data.forEach((item: any) => {
        if (count == 5) {
          return
        }
        scores.push({ score: item.Score, username: item.Username })
        count++
      })
    })
  })
})
</script>

<style scoped>
@font-face {
  font-family: sheepFont;
  src: url('../assets/fonts/sheep.ttf');
}

* {
  font-family: sheepFont;
}

#title {
  display: flex;
}

button {
  display: block;
  margin: auto;
  margin-top: 2rem;
  background: none;
  color: #c3c2bf;
  border: none;
}

button:hover {
  cursor: pointer;
}

#leaderboard {
  position: absolute;
  top: 0px;
  left: 0px;
  z-index: 100;
  text-align: center;
  width: 100vw;
}

#background-image-container {
  position: fixed;
  z-index: 0;
  top: 0px;
  left: 0px;
  background-color: black;
}

#background-image {
  width: 100vw;
  height: 100vh;
  background-image: url(../assets/images/leaderboard.jpg);
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-position: center;
  opacity: 0.5;
}

h1 {
  font-size: 10em;
}

p,
button {
  font-size: 5em;
}

button {
  transition: color 0.5s;
  color: #a6cbce;
}

button:hover {
  transition: color 0.5s;
  color: #3fc8d4;
}

.title {
  color: #a6cbce;
}

.leaderboard-item {
  color: #cc998d;
}
</style>
