<template>
  <div class="Myapp_question">
    <h1 id="header_question">{{ current_question_text }}</h1>
    <div id="one" class="image-container_question">
      <div class="image_question" @click="handleImageClick(1)">
        <!-- TODO: Static local images need to be updated -->
        <h2 class="imageLabel_question">{{ character_one_label}}</h2>
        <img :src="image1Src" alt="Image 1">
        
      </div>
      <div id="two" class="image_question" @click="handleImageClick(2)">
        <h2 class="imageLabel_question">{{ character_two_label}}</h2>
        <h2 class="scoreLabel_question">Score: {{ score }}</h2>
        <img :src="image2Src" alt="Image 2" >
        
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {ref} from 'vue'


let image1Src = ref(0);

let image2Src = ref(0);
let score = ref(0);

let questions : [];

var question_counter = 0;

let current_question_text = ref(0)

let character_one_label = ref(0);
let character_two_label = ref(0);

function handleImageClick(imageNumber:Number) {
      if (imageNumber == 1)
      {
        if (questions[question_counter]["Votes1"] >= questions[question_counter]["Votes2"])
        {
          //Load in next question and increment score
          question_counter++;
          updateQuestion()
          score.value++;
        }
        else{
          //Go to gameover screen, passing the final score
        }
      }
      else{
        if (questions[question_counter]["Votes2"] >= questions[question_counter]["Votes1"])
        {
          //Load in next question and increment score
          question_counter++;
          updateQuestion()
          score.value++;
        }
        else{
          //Go to gameover screen, passing the final score
        }
      }
      
    }


// function getMoreQuestions() {
//       var questions = fetch('https://unh4y7n697.execute-api.us-east-1.amazonaws.com/prod/questions');
//     }

async function getQuestions(){
  let response = await fetch('https://unh4y7n697.execute-api.us-east-1.amazonaws.com/prod/questions');
  questions = await response.json();
  image1Src.value = questions[question_counter]["Image1"];
  image2Src.value = questions[question_counter]["Image2"];
  current_question_text.value = questions[question_counter]["Question"];
  var char1_temp = questions[question_counter]["Image1"];
  var char2_temp = questions[question_counter]["Image2"];

  var char1_array = String(char1_temp).split("/")[1].split(".")[0].split("_");
  var char2_array = String(char2_temp).split("/")[1].split(".")[0].split("_");

  char1_temp = "";
  char2_temp = "";

  char1_array.forEach(element => {
    char1_temp += element + " "
  });

  char2_array.forEach(element => {
    char2_temp += element + " "
  });

  console.log(char1_temp);

  character_one_label.value = char1_temp;
  character_two_label.value = char2_temp;
}
getQuestions();


function updateQuestion(){
  image1Src.value = questions[question_counter]["Image1"];
  image2Src.value = questions[question_counter]["Image2"];
  current_question_text.value = questions[question_counter]["Question"];
  var char1_temp = questions[question_counter]["Image1"];
  var char2_temp = questions[question_counter]["Image2"];

  var char1_array = String(char1_temp).split("/")[1].split(".")[0].split("_");
  var char2_array = String(char2_temp).split("/")[1].split(".")[0].split("_");

  char1_temp = "";
  char2_temp = "";

  char1_array.forEach(element => {
    char1_temp += element + " "
  });

  char2_array.forEach(element => {
    char2_temp += element + " "
  });

  console.log(char1_temp);

  character_one_label.value = char1_temp;
  character_two_label.value = char2_temp;
}

// import image1Src from '../assets/images/testImage1.jpg';
// import image2Src from '../assets/images/testImage3.jpg';

// import questions from './questions.json';

// // var image1Src = questions[question_counter]["Image1"];
// // var image2Src = questions[question_counter]["Image2"];

// console.log(questions);

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
#header_question {
  text-align: center;
  color: #A6cbce;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 12%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  z-index: 1; /* Ensure the header appears in front of the images */
  font-size: 44pt;
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
  top: 75%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-size: 38pt;
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
