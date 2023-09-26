<template>
  <div class="Myapp_login">
    <h1 class="header_login">Herd Mentality</h1>
    <a @click="login" href="#">
      <img src="@/assets/google.svg" alt="Google Sign-In" class="google-svg" />
    </a>
    <div class="image-container_login">
      <div class="image_login">
        <img src="../assets/images/herd.jpg" alt="Flock of Sheep" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Auth } from 'aws-amplify'
import { CognitoHostedUIIdentityProvider } from '@aws-amplify/auth'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const LEADERBOARD_API = 'https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/leaderboard'

const router = useRouter()

async function login() {
  Auth.federatedSignIn({ provider: CognitoHostedUIIdentityProvider.Google })
}

onMounted(async () => {
  const currentUser = await Auth.currentAuthenticatedUser()
  console.log(currentUser);
  if (currentUser) {
    let response = await fetch(LEADERBOARD_API + "?user_id=" + currentUser.username, {
      method: 'GET',
      headers: {
        Authorization: 'Bearer ' + currentUser.signInUserSession.accessToken.jwtToken
      }
    })

    debugger

    var score = await response.json();
    score = parseInt(score['Score']);

    console.log("score: " + score);

    if (score != -1)
    {
      router.push('/');
    }
    else{
      router.push('/signup');
    }
    
  }
})
</script>

<style>
@font-face {
  font-family: sheepFont;
  src: url(../assets/fonts/sheep.ttf);
}

.header_login {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 20%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 130pt;
  color: #a6cbce;
}

#google_login {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 50%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  font-size: 100pt;
  z-index: 1;
  background: transparent;
  border: none;
  color: #cc998d;
}

#google_login:hover {
  font-size: 120pt;
  color: #dc816c;
}

/* Create a flex container to hold the images side by side */

.image-container_login {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0, 0, 0, 1);
}

/* Style for each image */
.image_login {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */
  background-size: cover; /* Scale the background image to cover the entire div */
  background-position: center; /* Center the background image within the div */
  /* height: 100vh; */

  overflow: hidden;
  position: relative;
}

.image_login img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

.google-svg {
  z-index: 2; /* Place it above the background image */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30%;
}

@media (max-width: 768px) {
  .header_login {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 20%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 60pt;
    color: #a6cbce;
  }

  #google_login {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 50%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-family: sheepFont;
    font-size: 100pt;
    z-index: 1;
    background: transparent;
    border: none;
    color: #cc998d;
  }

  #google_login:hover {
    font-size: 120pt;
    color: #dc816c;
  }

  /* Create a flex container to hold the images side by side */

  .image-container_login {
    display: flex;
    justify-content: space-between;
    height: 100vh;
    width: 200%;
    background-color: rgba(0, 0, 0, 1);
  }

  /* Style for each image */
  .image_login {
    flex: 1; /*Each image takes up an equal part of the container*/
    text-align: center; /* Center the content horizontally */
    background-size: cover; /* Scale the background image to cover the entire div */
    background-position: center; /* Center the background image within the div */
    /* height: 100vh; */

    overflow: hidden;
    position: relative;
  }

  .image_login img {
    height: 100%;
    width: 100%;
    object-fit: cover;
    background-color: transparent;
    opacity: 0.5;
  }

  .google-svg {
    z-index: 2; /* Place it above the background image */
    position: absolute;
    top: 60%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 75%;
  }
}
</style>
