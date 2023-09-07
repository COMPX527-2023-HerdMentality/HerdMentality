
<template>
    <!--https://beginnersoftwaredeveloper.com/how-do-i-navigate-between-views-on-my-vue-router/-->
    <div class="Myapp">
        <h1 class="header">Herd Mentality</h1>

        <router-link to="/account"><input id="account" type="button" value="Account"></router-link>
        <router-link to="/play"><input id="play" type="button" value="Play"></router-link>
        <router-link to="/leaderboard"><input id="leaderboard" type="button" value="Leaderboard"></router-link>

        <div class="image-container">
            <div class="image">
                <!-- Your first image goes here -->
                <img src="../assets/images/herd.jpg" alt="Flock of Sheep">
            </div>
        </div>
    </div>
</template>


/* Center the header text vertically and horizontally */
<style>

@font-face {
    font-family: sheepFont;
    src: url(../assets/fonts/sheep.ttf);
}

.header {
text-align: center;
position: absolute; /* Position the header absolutely within the .Myapp container */
top: 20%; /* Center vertically */
left: 50%; /* Center horizontally */
transform: translate(-50%, -50%); /*Center the header perfectly*/
z-index: 1; /* Ensure the header appears in front of the images */
font-family: sheepFont;
font-size: 130pt;
color: #A6CBCE;
}

#play, #leaderboard, #account{
    text-align: center;
position: absolute; /* Position the header absolutely within the .Myapp container */
top: 40%; /* Center vertically */
left: 50%; /* Center horizontally */
transform: translate(-50%, -50%); /*Center the header perfectly*/
font-family: sheepFont;
font-size: 100pt;
z-index: 1;
background: transparent;
border: none;
color: #cc998d;
}

#leaderboard{
    top:60%;
    font-size: 80pt;
}

#account{
    top:80%;
    font-size: 60pt;
}

#play:hover{
    font-size: 120pt;
    color: #DC816C;
}

#account:hover{
    font-size: 80pt;
    color: #DC816C;
}

#leaderboard:hover{
    font-size: 100pt;
    color: #DC816C;
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
  text-align: center; /* Center the content horizontally */
  background-size: cover; /* Scale the background image to cover the entire div */
  background-position: center; /* Center the background image within the div */
  /* height: 100vh; */
  
  overflow: hidden;
  position: relative;
}

.image img{
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}
</style>