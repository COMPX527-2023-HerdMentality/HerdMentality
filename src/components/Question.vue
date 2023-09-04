<template>
  <div class="Myapp">
    <h1 class="header">Question???</h1>
    <div class="image-container">
      <div class="image">
        <!-- Your first image goes here -->
        <img src="../assets/images/testImage1.jpg" alt="Image 1">
      </div>
      <div class="image">
        <!-- Your second image goes here -->
        <img src="../assets/images/testImage3.jpg" alt="Image 2">
      </div>
    </div>
  </div>
</template>

<style>
.Myapp {
  width: 100%;
}

/* Center the header text vertically and horizontally */
.header {
  text-align: center;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 10%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  z-index: 1; /* Ensure the header appears in front of the images */
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
  opacity: 0.75;
}

</style>