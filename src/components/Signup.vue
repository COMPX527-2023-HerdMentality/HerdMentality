<template>
  <div class="Myapp_signup">
    <h1 class="header_signup">Herd Mentality</h1>
    <h2 class="signup_label">Create Username:</h2>
    <form @submit.prevent="postUsername">
      <input type="text" id="signup_username_box" ref="usernameInput" />
      <input type="submit" value="Continue" id="signup_username_submit" />
    </form>
    <div class="image-container_signup">
      <div class="image_signup">
        <img src="../assets/images/herd.jpg" alt="Flock of Sheep" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Auth } from 'aws-amplify'
import { CognitoHostedUIIdentityProvider } from '@aws-amplify/auth'
import { onMounted, toValue } from 'vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const usernameInput = ref('')

const LEADERBOARD_API = 'https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/leaderboard'

const router = useRouter()

async function login() {
  Auth.federatedSignIn({ provider: CognitoHostedUIIdentityProvider.Google })
}

async function postUsername() {
  try {
    const currentUser = await Auth.currentAuthenticatedUser()

    var userNameValue = document.querySelector('#signup_username_box') as HTMLInputElement | null

    var userName = userNameValue?.value

    if (currentUser) {
      console.log(usernameInput.value)

      let response = await fetch(LEADERBOARD_API, {
        method: 'POST',
        headers: {
          Authorization: 'Bearer ' + currentUser.signInUserSession.accessToken.jwtToken
        },
        body: JSON.stringify({ score: Number(0), username: userName })
      })

      debugger
    }

    // Handle the response from the Lambda function here
  } catch (error) {
    // Handle any errors that occur during the request
    console.error('Error sending POST request to Lambda:', error)
  }
  router.push('/')
}

onMounted(async () => {
  const currentUser = await Auth.currentAuthenticatedUser()
})
</script>

<style>
@font-face {
  font-family: sheepFont;
  src: url(../assets/fonts/sheep.ttf);
}

.header_signup {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 20%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 110pt;
  color: #a6cbce;
}

#signup_username_box {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 50%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-size: 40pt;
  z-index: 5;
}

#signup_username_submit {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 65%; /* Center vertically */
  left: 50%; /* Center horizontally */
  font-family: sheepFont;
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-size: 50pt;
  color: #dc816c;
  z-index: 5;
  background-color: rgba(163, 163, 163, 0);
  border-width: 0pt;
}

#signup_username_submit:hover {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 65%; /* Center vertically */
  left: 50%; /* Center horizontally */
  font-family: sheepFont;
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-size: 70pt;
  color: #dc816c;
  z-index: 5;
  background-color: rgba(163, 163, 163, 0);
  border-width: 0pt;
}

.signup_label {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 35%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 70pt;
  color: #a6cbce;
}

#google_signup {
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

/* Create a flex container to hold the images side by side */

.image-container_signup {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0, 0, 0, 1);
}

/* Style for each image */
.image_signup {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */
  background-size: cover; /* Scale the background image to cover the entire div */
  background-position: center; /* Center the background image within the div */
  /* height: 100vh; */

  overflow: hidden;
  position: relative;
}

.image_signup img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

@media (max-width: 768px) {
  .header_signup {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 20%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 40pt;
    color: #a6cbce;
  }

  .signup_label {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 40%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 20pt;
    color: #a6cbce;
  }

  #signup_username_box {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 50%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-size: 18pt;
    z-index: 5;
  }

  #google_signup {
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

  #google_signup:hover {
    font-size: 120pt;
    color: #dc816c;
  }

  #signup_username_submit {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 65%; /* Center vertically */
    left: 50%; /* Center horizontally */
    font-family: sheepFont;
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-size: 40pt;
    color: #dc816c;
    z-index: 5;
    background-color: rgba(163, 163, 163, 0);
    border-width: 0pt;
  }

  #signup_username_submit:hover {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 65%; /* Center vertically */
    left: 50%; /* Center horizontally */
    font-family: sheepFont;
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-size: 60pt;
    color: #dc816c;
    z-index: 5;
    background-color: rgba(163, 163, 163, 0);
    border-width: 0pt;
  }

  /* Create a flex container to hold the images side by side */

  .image-container_signup {
    display: flex;
    justify-content: space-between;
    height: 100vh;
    width: 200%;
    background-color: rgba(0, 0, 0, 1);
  }

  /* Style for each image */
  .image_signup {
    flex: 1; /*Each image takes up an equal part of the container*/
    text-align: center; /* Center the content horizontally */
    background-size: cover; /* Scale the background image to cover the entire div */
    background-position: center; /* Center the background image within the div */
    /* height: 100vh; */

    overflow: hidden;
    position: relative;
  }

  .image_signup img {
    height: 100%;
    width: 100%;
    object-fit: cover;
    background-color: transparent;
    opacity: 0.5;
  }
}
</style>
