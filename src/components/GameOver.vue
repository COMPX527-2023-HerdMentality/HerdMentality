<template>
    <div class="Myapp">
      <h1 class="title">GAME OVER</h1>
      <h2 class="score">Score: </h2>
      <h2 class="highScore">High Score: {{ score }}</h2>
      <input id="playAgain" type="button" value="Play Again" @click="playAgainClick()"> 
      <div class="image-container">
        <div class="image">
          <!-- Your first image goes here -->
          <img src="../assets/images/gameOverImage.avif" alt="Image 1">
        </div>
      </div>
    </div>
  </template>
  
<script>

export default {
    data() {
        return {
            score: 0
        };
    },
    methods: {
        playAgainClick() {
            this.score++;
        }
    }
};

</script>

  <style>
  .Myapp {
    width: 100%;
  }
  
  /* Center the header text vertically and horizontally */
  .title {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 10%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    color: white;
  }

  .score {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 40%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    color: white;
  }

  .highScore {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 45%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    color: white;
  }

  #playAgain {
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 55%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-size: 50pt;
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