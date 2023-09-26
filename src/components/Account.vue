<template>
  <div class="Myapp_account">
    <h1 class="header_account">Account</h1>
    <a @click="signOut" href="#">
      <input id="signout_account" type="button" value="Sign Out" />
    </a>
    <input id="delete_account" type="button" value="Delete Account" />
    <router-link to="/"><input id="back_account" type="button" value="Back" /></router-link>

    <div class="image-container_account">
      <div class="image_account">
        <!-- Your first image goes here -->
        <img src="../assets/images/herd.jpg" alt="Image 1" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Auth } from 'aws-amplify'

async function signOut() {
  try {
    console.log()
    await Auth.signOut()
  } catch (error) {
    console.log('error signing out: ', error)
  }
}

// async function deleteUser() {
//   try {
//     const result = await Auth.deleteUser();
//     console.log(result);
//   } catch (error) {
//     console.log('Error deleting user', error);
//   }
// }
</script>

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
  color: #a6cbce;
}

#signout_account {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 45%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  font-size: 60pt;
  z-index: 1;
  background: transparent;
  border: none;
  color: #cc998d;
}

#signout_account:hover {
  font-size: 80pt;
  color: #dc816c;
}

#delete_account {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 60%; /* Center vertically */
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
  color: #dc816c;
}

#back_account {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 75%; /* Center vertically */
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
  color: #dc816c;
}

/* Create a flex container to hold the images side by side */

.image-container_account {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0, 0, 0, 1);
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

.image_account img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

@media (max-width: 768px) {
  .header_account {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 20%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    z-index: 1; /* Ensure the header appears in front of the images */
    font-family: sheepFont;
    font-size: 70pt;
    color: #a6cbce;
  }

  #signout_account {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 45%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-family: sheepFont;
    font-size: 50pt;
    z-index: 1;
    background: transparent;
    border: none;
    color: #cc998d;
  }

  #signout_account:hover {
    font-size: 70pt;
    color: #dc816c;
  }

  #delete_account {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 60%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-family: sheepFont;
    font-size: 50pt;
    z-index: 1;
    background: transparent;
    border: none;
    color: #cc998d;
  }

  #delete_account:hover {
    font-size: 80pt;
    color: #dc816c;
  }

  #back_account {
    text-align: center;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 75%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-family: sheepFont;
    font-size: 50pt;
    z-index: 1;
    background: transparent;
    border: none;
    color: #cc998d;
  }

  #back_account:hover {
    font-size: 80pt;
    color: #dc816c;
  }

  /* Create a flex container to hold the images side by side */

  .image-container_account {
    display: flex;
    justify-content: space-between;
    height: 100vh;
    width: 200%;
    background-color: rgba(0, 0, 0, 1);
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

  .image_account img {
    height: 100%;
    width: 100%;
    object-fit: cover;
    background-color: transparent;
    opacity: 0.5;
  }
}
</style>
