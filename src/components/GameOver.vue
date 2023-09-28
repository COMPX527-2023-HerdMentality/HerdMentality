<template>
  <div class="Myapp_gameover">
    <h1 class="header_gameover">GAME OVER</h1>
    <h2 class="score_gameover">Score: {{ score }}</h2>
    <h2 class="highScore_gameover">High Score: {{ highScore }}</h2>
    <router-link to="/play"
      ><input id="play_gameover" type="button" value="Play Again"
    /></router-link>
    <router-link to="/leaderboard"
      ><input id="leaderboard_gameover" type="button" value="Leaderboard"
    /></router-link>
    <router-link to="/"><input id="home_gameover" type="button" value="Home" /></router-link>
    <div class="image-container_gameover">
      <div class="image_gameover">
        <!-- Your first image goes here -->
        <img src="../assets/images/gameOverImage.avif" alt="Image 1" />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { Auth } from 'aws-amplify'
import { useRoute } from 'vue-router'
import { onMounted, reactive, ref } from 'vue'
// const topicArn = 'arn:aws:sns:us-east-1:760360511766:leaderboard_notifier';
// const message = 'Someone has just entered the leaderboard, jump back in now to secure your position!';

// // Create an AWS service instance (e.g., SNS)
// const sns = new AWS.SNS();

// sns.publish({
//   TopicArn: topicArn,
//   Message: message,
// }, (err, data) => {
//   if (err) {
//     console.error('Error publishing message:', err);
//   } else {
//     console.log('Message published successfully:', data);
//   }
// });

let highScore = ref(0)
// highScore = 3

const route = useRoute()
const score = reactive<Number>(Number(window.localStorage.getItem('score')))

const LEADERBOARD_API = 'https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/leaderboard'

onMounted(async () => {
  console.log(route)
  const user = await Auth.currentAuthenticatedUser()
  if (user) {
    fetch('https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/leaderboard', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + user.signInUserSession.accessToken.jwtToken
      },
      body: JSON.stringify({ score: score })
    })

    fetch('https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/notify', {
      method: 'POST',
      body: JSON.stringify({ email: user.attributes.email })
    })

    let response = await fetch(LEADERBOARD_API + '?user_id=' + user.username, {
      method: 'GET',
      headers: {
        Authorization: 'Bearer ' + user.signInUserSession.accessToken.jwtToken
      }
    })

    var highScoreResponse = await response.json()
    highScore.value = parseInt(highScoreResponse['Score'])
  }
})
</script>

<style>
@font-face {
  font-family: sheepFont;
  src: url(../assets/fonts/sheep.ttf);
}

.Myapp_gameover {
  width: 100%;
}

/* Center the header text vertically and horizontally */
.header_gameover {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 20%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 100pt;
  color: #a6cbce;
}

.score_gameover {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 40%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 80pt;
  color: #a6cbce;
}

.highScore_gameover {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 50%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  color: #cc998d;
}

#play_gameover {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 65%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 70pt;
  background-color: transparent;
  border: none;
  color: #cc998d;
}

#play_gameover:hover {
  font-size: 80pt;
  color: #dc816c;
}

#leaderboard_gameover {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 75%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  background-color: transparent;
  border: none;
  color: #cc998d;
}

#leaderboard_gameover:hover {
  font-size: 60pt;
  color: #dc816c;
}

#home_gameover {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 85%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  background-color: transparent;
  border: none;
  color: #cc998d;
}

#home_gameover:hover {
  font-size: 60pt;
  color: #dc816c;
}

/* Create a flex container to hold the images side by side */
.image-container_gameover {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0, 0, 0, 1);
}

/* Style for each image */
.image_gameover {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */
  /* background-size: cover; Scale the background image to cover the entire div */
  background-position: 0%; /* Center the background image within the div */
  overflow: hidden;
  position: relative;
}

.image_gameover img {
  height: auto;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

@media (max-width: 768px) {
  .Myapp_gameover {
    width: 100%;
  }

  /* Center the header text vertically and horizontally */
  .header_gameover {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 15%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 35pt;
    color: #a6cbce;
  }

  .score_gameover {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 25%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 30pt;
    color: #a6cbce;
  }

  .highScore_gameover {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 35%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 30pt;
    color: #cc998d;
  }

  #play_gameover {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 55%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 50pt;
    background-color: transparent;
    border: none;
    color: #cc998d;
  }

  #play_gameover:hover {
    font-size: 70pt;
    color: #dc816c;
  }

  #leaderboard_gameover {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 70%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 50pt;
    background-color: transparent;
    border: none;
    color: #cc998d;
  }

  #leaderboard_gameover:hover {
    font-size: 60pt;
    color: #dc816c;
  }

  #home_gameover {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 85%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 50pt;
    background-color: transparent;
    border: none;
    color: #cc998d;
  }

  #home_gameover:hover {
    font-size: 60pt;
    color: #dc816c;
  }

  /* Create a flex container to hold the images side by side */
  .image-container_gameover {
    display: flex;
    justify-content: space-between;
    height: 100vh;
    width: 200%;
    background-color: rgba(0, 0, 0, 1);
  }

  /* Style for each image */
  .image_gameover {
    flex: 1; /*Each image takes up an equal part of the container*/
    text-align: center; /* Center the content horizontally */
    background-size: cover; /*Scale the background image to cover the entire div */
    background-position: 0%; /* Center the background image within the div */
    overflow: hidden;
    position: relative;
  }

  .image_gameover img {
    height: 100%;
    width: 100%;
    object-fit: cover;
    background-color: transparent;
    opacity: 0.5;
    object-position: 90% center; /* Adjust the horizontal offset as needed */
  }
}
</style>
