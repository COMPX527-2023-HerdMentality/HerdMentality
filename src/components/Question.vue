<template>
  <div class="Myapp_question">
    <h1 class="header_question">Who is most likely to be the most scared while watching a horror movie?</h1>
    <div class="image-container_question">
      <div class="image_question" @click="handleImageClick(1)">
        <!-- TODO: Static local images need to be updated -->
        <h2 class="imageLabel_question">Image 1</h2>
        <img :src="image1Src" alt="Image 1">
        
      </div>
      <div class="image_question" @click="handleImageClick(2)">
        <h2 class="imageLabel_question">Image 2</h2>
        <h2 class="scoreLabel_question">Score: {{ score }}</h2>
        <img :src="image2Src" alt="Image 2" >
        
      </div>
    </div>
  </div>
</template>

<script>
import image1Src from '../assets/images/testImage1.jpg';
import image2Src from '../assets/images/testImage3.jpg';

export default {
  data() {
    return {
      image1Src,
      image2Src,
      score: 0,
    };
  },
  methods: {
    handleImageClick(imageNumber) {
      // Swap the image sources when Image 1 is clicked
      if (imageNumber == 1)
      {
        const tempSrc = this.image1Src;
        this.image1Src = this.image2Src;
        this.image2Src = tempSrc;
        this.score++;
      }
      else{

      }
      
    },
  },
};
</script>

<style>

@font-face{
  font-family: sheepFont;
  src: url(../assets/fonts/sheep.ttf)
}
.Myapp_question {
  width: 100%;
}

/* Center the header text vertically and horizontally */
.header_question {
  text-align: center;
  color: #A6cbce;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 12%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  z-index: 1; /* Ensure the header appears in front of the images */
  font-size: 36pt;
}

/* Create a flex container to hold the images side by side */
.image-container_question {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0,0,0,1);

}

/* Style for each image */
.image_question {
  flex: 1; /*Each image takes up an equal part of the container*/
  text-align: center; /* Center the content horizontally */
  background-size: cover; /* Scale the background image to cover the entire div */
  background-position: center; /* Center the background image within the div */
  /* height: 100vh; */
  
  overflow: hidden;
  position: relative;
}

.image_question img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  background-color: transparent;
  opacity: 0.5;
}

.imageLabel_question {
  color: #A6cbce;
  z-index: 1; /* Ensure the header appears in front of the images */
  position: absolute; /* Position the header absolutely within the .Myapp container */
  text-align: center;
  top: 60%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-size: 26pt;
  font-family: sheepFont;
}

.scoreLabel_question {
  color: #CC998D;
  z-index: 1; /* Ensure the header appears in front of the images */
  position: absolute; /* Position the header absolutely within the .Myapp container */
  text-align: center;
  top: 97%; /* Center vertically */
  left: 87%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  font-size: 26pt;
}

</style>