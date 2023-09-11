<template>
  <div class="Myapp">
    <h1 class="leaderboard">Leaderboard</h1>
    <h2 class="score1">User: {{ score }}</h2>
    <h2 class="score2">User: {{ score }}</h2>
    <h2 class="score3">User: {{ score }}</h2>
    <h2 class="score4">User: {{ score }}</h2>
    <h2 class="score5">User: {{ score }}</h2>
    <h2 class="highScore">Your Highscore: {{ highScore }}</h2>
    <router-link to="/play"><input id="play_leaderboard" type="button" value="Play"></router-link>
    <router-link to="/"><input id="home_leaderboard" type="button" value="Home"></router-link>
    <div class="image-container">
      <div class="image">
        <!-- Your first image goes here -->
        <img src="../assets/images/gameOverImage.avif" alt="Image 1">
      </div>
    </div>
  </div>
</template>More navigation added and delete account button made.

<script lang="ts">

export default {
  data() {
      return {
          highScore: 0,
          score: 0
      };
  },
  methods: {
      playClick() {
          this.highScore++;
      },
  }
};

</script>


<style>

@font-face {
  font-family: sheepFont;
  src: url(../assets/fonts/sheep.ttf);
}

.Myapp {
  width: 100%;
}

/* Center the header text vertically and horizontally */
.leaderboard {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 13%; /* Center vertically */

  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 110pt;
  color: #CC998D;
}

.score1 {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 30%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 90pt;
  color: #A6CBCE;
}

.score2 {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 40%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 75pt;
  color: #A6CBCE;
}

.score3 {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 49%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 60pt;
  color: #A6CBCE;
}

.score4 {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 57%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  color: #A6CBCE;
}

.score5 {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 64%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  color: #A6CBCE;
}

.highScore {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 76%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  color: #CC998D;
}

#play_leaderboard {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 90%; /* Center vertically */
  left: 30%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 70pt;
  background-color: transparent;
  border: none;
  color: #CC998D;
}

#play_leaderboard:hover {
  font-size: 80pt;
  color: #DC816C
}

#home_leaderboard {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 90%; /* Center vertically */
  left: 70%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 70pt;
  background-color: transparent;
  border: none;
  color: #CC998D;
}

#home_leaderboard:hover {
  font-size: 80pt;
  color: #DC816C
}

#leaderboards {
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 82%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
  font-family: sheepFont;
  font-size: 50pt;
  background-color: transparent;
  border: none;
  color: #CC998D;
}

#leaderboards:hover {
  font-size: 60pt;
  color: #DC816C
}

/* Create a flex container to hold the images side by side */
.image-container {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0,0,0,1);
}

/* Style for each image */
.image {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */;
  /* background-size: cover; Scale the background image to cover the entire div */
  background-position: 0%; /* Center the background image within the div */    
  overflow: hidden;
  position: relative;
}

.image img{
  height: auto;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

</style>
