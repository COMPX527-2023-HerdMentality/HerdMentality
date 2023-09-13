<template>
    <div class="Myapp_account">
        <h1 class="header_account">Account</h1>

        <input id="delete_account" type="button" value="Delete Account">
        <router-link to="/"><input id="back_account" type="button" value="Back"></router-link>

        <div class="image-container_account">
            <div class="image_account">
                <!-- Your first image goes here -->
                <img src="../assets/images/herd.jpg" alt="Image 1">
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

.header_account {
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

#delete_account {
    text-align: center;
position: absolute; /* Position the header absolutely within the .Myapp container */
top: 65%; /* Center vertically */
left: 50%; /* Center horizontally */
transform: translate(-50%, -50%); /*Center the header perfectly*/
font-family: sheepFont;
font-size: 60pt;
z-index: 1;
background: transparent;
border: none;
color: #cc998d;
}

#delete_account:hover {
    font-size: 80pt;
    color: #DC816C;
}

#back_account {
    text-align: center;
position: absolute; /* Position the header absolutely within the .Myapp container */
top: 80%; /* Center vertically */
left: 50%; /* Center horizontally */
transform: translate(-50%, -50%); /*Center the header perfectly*/
font-family: sheepFont;
font-size: 60pt;
z-index: 1;
background: transparent;
border: none;
color: #cc998d;
}

#back_account:hover {
    font-size: 80pt;
    color: #DC816C;
}

/* Create a flex container to hold the images side by side */

.image-container_account {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0,0,0,1);

}

/* Style for each image */
.image_account {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */
  background-size: cover; /* Scale the background image to cover the entire div */
  background-position: center; /* Center the background image within the div */
  /* height: 100vh; */
  
  overflow: hidden;
  position: relative;
}

.image_account img{
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}
</style>