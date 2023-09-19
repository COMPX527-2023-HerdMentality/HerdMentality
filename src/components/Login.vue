
<template>
    <div class="Myapp_login">
        <h1 class="header_login">Herd Mentality</h1>
        <a v-if="hostname == 'localhost'" href="https://herdmentality.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=4evgbmouciqv3vodnoafsp4rag&response_type=code&scope=email+openid+phone&redirect_uri=http://localhost:5173">
            <img src="@/assets/google.svg" alt="Google Sign-In" class="google-svg" />
        </a>
        <a v-else href="https://herdmentality.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=4evgbmouciqv3vodnoafsp4rag&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fd26uos70b4pzd2.cloudfront.net">
            <img src="@/assets/google.svg" alt="Google Sign-In" class="google-svg" />
        </a>
        <div class="image-container_login">
            <div class="image_login">
                <img src="../assets/images/herd.jpg" alt="Flock of Sheep">
            </div>
        </div>
    </div>
</template>


<script setup lang="ts">

    const hostname = window.location.hostname;
    import googleSvg from '@/assets/google.svg';
    console.log(window.location.hostname);

    export default {
        data() {
            return {
                hostname,
                googleSvg,
            };
        },
    };
    // import {CognitoUserPool} from "amazon-cognito-identity-js"
    import {ref} from 'vue';
    const hostname = ref("");
    hostname.value = window.location.hostname;
    
    const hash = window.location.hash.substr(1);
    if(hash != "" && hash.includes("access_token=")){
        // Submit the access token to our API endpoint to have it returned in an httpOnly cookie
        fetch("https://unh4y7n697.execute-api.us-east-1.amazonaws.com/prod/login?"+hash);
    }
    
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
<<<<<<< HEAD

.google-svg{
    z-index: 2; /* Place it above the background image */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width:30%;
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

.google-svg{
    z-index: 2; /* Place it above the background image */
    position: absolute;
    top: 60%;
    left: 50%;
    transform: translate(-50%, -50%);
    width:75%;
}
}
</style>
=======
</style>
>>>>>>> c929fe7 (working on persisting login)
