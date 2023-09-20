
<template>

    <link rel="typescript"  src="preload.ts" />

    <!--https://beginnersoftwaredeveloper.com/how-do-i-navigate-between-views-on-my-vue-router/-->
    <div class="Myapp_home">
        <h1 class="header_home">Herd Mentality</h1>

        <router-link to="/account"><input id="account_home" type="button" value="Account"></router-link>
        <router-link to="/play"><input id="play_home" type="button" value="Play"></router-link>
        <router-link to="/leaderboard"><input id="leaderboard_home" type="button" value="Leaderboard"></router-link>

        

        <div class="image-container_home">
            <div class="image_home">
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

.header_home {
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

#play_home, #leaderboard_home, #account_home {
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

#leaderboard_home {
    top:60%;
    font-size: 80pt;
}

#account_home {
    top:80%;
    font-size: 60pt;
}

#play_home:hover {
    font-size: 120pt;
    color: #DC816C;
}

#account_home:hover {
    font-size: 80pt;
    color: #DC816C;
}

#leaderboard_home:hover {
    font-size: 100pt;
    color: #DC816C;
}

/* Create a flex container to hold the images side by side */

.image-container_home {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0,0,0,1);

}

/* Style for each image */
.image_home {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */
  background-size: cover; /* Scale the background image to cover the entire div */
  background-position: center; /* Center the background image within the div */
  /* height: 100vh; */
  
  overflow: hidden;
  position: relative;
}

.image_home img{
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

@media (max-width: 768px) {
    .header_home {
        font-size: 40pt;
        top: 25%; /* Center vertically */
        /* Add any other necessary adjustments */
    }

    #play_home, #leaderboard_home, #account_home {
        font-size: 30pt;
        /* Add any other necessary adjustments */
        top: 45%;
    }

    #leaderboard_home {
        top: 55%;
        font-size: 32pt;
    }

    #account_home {
        top: 65%;
        font-size: 24pt;
    }

    .image-container_home {
        display: flex;
        justify-content: space-between;
        height: 100vh;
        width: 200%;
        background-color: rgba(0,0,0,1);
    }

    /* Style for each image */
    .image_home {
        flex: 1; /*Each image takes up an equal part of the container*/
        text-align: center; /* Center the content horizontally */
        background-size: cover; /* Scale the background image to cover the entire div */
        background-position: center; /* Center the background image within the div */
        /* height: 100vh; */
        
        overflow: hidden;
        position: relative;
    }

    .image_home img{
        height: 100%;
        width: 100%;
        object-fit: cover;
        background-color: transparent;
        opacity: 0.5;
    }
}
</style>