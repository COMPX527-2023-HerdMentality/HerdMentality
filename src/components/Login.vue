
<template>
    <div class="Myapp_login">
        <h1 class="header_login">Herd Mentality</h1>

        <a v-if="hostname == 'localhost'" href="https://herdmentality.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=4evgbmouciqv3vodnoafsp4rag&response_type=code&scope=email+openid+phone&redirect_uri=http://localhost:5173">
            <input id="google_login" type="button" value="Sign in with Google">
        </a>
        <a v-else href="https://herdmentality.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=4evgbmouciqv3vodnoafsp4rag&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fd26uos70b4pzd2.cloudfront.net">
            <input id="google_login" type="button" value="Sign in with Google">
        </a>
        <div class="image-container_login">
            <div class="image_login">
                <img src="../assets/images/herd.jpg" alt="Flock of Sheep">
            </div>
        </div>
    </div>
</template>


<script lang="ts">

    const hostname = window.location.hostname;
    console.log(window.location.hostname);

    export default {
        data() {
            return {
                hostname,
            };
        },
    };
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
color: #A6CBCE;
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
    color: #DC816C;
}

/* Create a flex container to hold the images side by side */

.image-container_login {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0,0,0,1);

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

.image_login img{
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}
</style>