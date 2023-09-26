<template>
  <div class="Myapp_question">
    <h1 id="header_question">{{ current_question_text }}</h1>
    <div class="image-container_question">
      <div id="left_image" class="image_question" @click="handleImageClick(1)">
        <!-- TODO: Static local images need to be updated -->
        <h2 class="imageLabel_question">{{ character_one_label }}</h2>
        <img :src="image1Src" alt="Image 1" />
        <div id="left_transition_div" class="transition_inactive"></div>
      </div>

      <div id="right_image" class="image_question" @click="handleImageClick(2)">
        <h2 class="imageLabel_question">{{ character_two_label }}</h2>
        <h2 class="scoreLabel_question">Score: {{ score }}</h2>
        <img :src="image2Src" alt="Image 2" />
        <div id="right_transition_div" class="transition_inactive"></div>
      </div>
    </div>
    <img id="temp1" :src="temp1" alt="temp1" />
    <img id="temp2" :src="temp2" alt="temp2" />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const QUESTIONS_API = 'https://rvunpy4go9.execute-api.us-east-1.amazonaws.com/prod/questions'
//Preloading images setup
let temp1 = ref('')
let temp2 = ref('')

let image1Src = ref('')

let image2Src = ref('')
let score = ref(0)

let questions: any

var question_counter = 0

var timeout_active = false

let current_question_text = ref('')

let character_one_label = ref('')
let character_two_label = ref('')

function handleImageClick(imageNumber: Number) {
  if (timeout_active) {
    return
  }

  var total_votes =
    parseInt(questions[question_counter]['Votes1']) +
    parseInt(questions[question_counter]['Votes2'])
  var percent_for_one = (parseFloat(questions[question_counter]['Votes1']) / total_votes) * 100
  var percent_for_two = (parseFloat(questions[question_counter]['Votes2']) / total_votes) * 100

  character_one_label.value = character_one_label.value + '\n' + percent_for_one.toFixed(2) + '%'
  character_two_label.value = character_two_label.value + '\n' + percent_for_two.toFixed(2) + '%'

  //set heights for transition divs
  var leftTransitionDiv = document.getElementById('left_transition_div')
  if (leftTransitionDiv !== null) {
    leftTransitionDiv.style.height = percent_for_one + '%'
  }

  var rightTransitionDiv = document.getElementById('right_transition_div')
  if (rightTransitionDiv !== null) {
    rightTransitionDiv.style.height = percent_for_two + '%'
  }

  document.getElementById('left_transition_div')?.classList.remove('transition_inactive')
  document.getElementById('right_transition_div')?.classList.remove('transition_inactive')

  if (imageNumber == 1) {
    postAnswer(1)
    if (questions[question_counter]['Votes1'] >= questions[question_counter]['Votes2']) {
      //Load in next question and increment score
      question_counter++

      score.value++

      document.getElementById('left_transition_div')?.classList.add('transition_correct')
      document.getElementById('right_transition_div')?.classList.add('transition_incorrect')

      timeout_active = true

      setTimeout(updateQuestion, 2500)
    } else {
      //Go to gameover screen, passing the final score
      //document.getElementById("left_image")?.classList.add("container-transition-wrong");
      document.getElementById('left_transition_div')?.classList.add('transition_incorrect')
      timeout_active = true
      setTimeout(() => {
        //Pass a parameter as part of the route's URL
        router.push({ name: 'gameover', params: { score: score.value } })
      }, 2500)

      document.getElementById('left_transition_div')?.classList.add('transition_incorrect')
      document.getElementById('right_transition_div')?.classList.add('transition_correct')
    }
  } else {
    postAnswer(2)
    if (questions[question_counter]['Votes2'] >= questions[question_counter]['Votes1']) {
      //Load in next question and increment score
      question_counter++

      score.value++
      //document.getElementById("right_image")?.classList.add("container-transition-correct");
      document.getElementById('right_transition_div')?.classList.add('transition_correct')
      timeout_active = true

      setTimeout(updateQuestion, 2500)
      document.getElementById('left_transition_div')?.classList.add('transition_incorrect')
      document.getElementById('right_transition_div')?.classList.add('transition_correct')
    } else {
      //Go to gameover screen, passing the final score
      //document.getElementById("right_image")?.classList.add("container-transition-wrong");
      document.getElementById('right_transition_div')?.classList.add('transition_incorrect')
      timeout_active = true
      setTimeout(() => {
        //Pass a parameter as part of the route's URL
        router.push({ name: 'gameover', params: { score: score.value } })
      }, 2500)
      document.getElementById('left_transition_div')?.classList.add('transition_correct')
      document.getElementById('right_transition_div')?.classList.add('transition_incorrect')
    }
  }
}

async function getQuestions() {
  let response = await fetch(QUESTIONS_API)
  questions = await response.json()
  image1Src.value = questions[question_counter]['Image1']
  image2Src.value = questions[question_counter]['Image2']

  //Getting images for next question
  temp1.value = questions[question_counter + 1]['Image1']
  temp2.value = questions[question_counter + 1]['Image2']

  console.log(temp1.value)
  console.log(temp2.value)

  current_question_text.value = questions[question_counter]['Question']
  let char1_temp = questions[question_counter]['Image1']
  let char2_temp = questions[question_counter]['Image2']

  var char1_array = String(char1_temp).split('/')[1].split('.')[0].split('_')
  var char2_array = String(char2_temp).split('/')[1].split('.')[0].split('_')

  char1_temp = ''
  char2_temp = ''

  char1_array.forEach((element) => {
    char1_temp += element + ' '
  })

  char2_array.forEach((element) => {
    char2_temp += element + ' '
  })

  console.log(char1_temp)

  character_one_label.value = char1_temp
  character_two_label.value = char2_temp
}
getQuestions()

function updateQuestion() {
  image1Src.value = temp1.value
  image2Src.value = temp2.value

  //Preload next images
  temp1.value = questions[question_counter + 1]['Image1']
  temp2.value = questions[question_counter + 1]['Image2']

  current_question_text.value = questions[question_counter]['Question']
  var char1_temp = questions[question_counter]['Image1']
  var char2_temp = questions[question_counter]['Image2']

  var char1_array = String(char1_temp).split('/')[1].split('.')[0].split('_')
  var char2_array = String(char2_temp).split('/')[1].split('.')[0].split('_')

  char1_temp = ''
  char2_temp = ''

  char1_array.forEach((element) => {
    char1_temp += element + ' '
  })

  char2_array.forEach((element) => {
    char2_temp += element + ' '
  })

  console.log(char1_temp)

  character_one_label.value = char1_temp
  character_two_label.value = char2_temp

  // document.getElementById("right_image")?.classList.remove("container-transition-correct");
  // document.getElementById("right_image")?.classList.remove("container-transition-wrong");
  // document.getElementById("left_image")?.classList.remove("container-transition-correct");
  // document.getElementById("left_image")?.classList.remove("container-transition-wrong");
  document.getElementById('left_transition_div')?.classList.remove('transition_correct')
  document.getElementById('left_transition_div')?.classList.remove('transition_incorrect')
  document.getElementById('left_transition_div')?.classList.add('transition_inactive')
  document.getElementById('right_transition_div')?.classList.remove('transition_correct')
  document.getElementById('right_transition_div')?.classList.remove('transition_incorrect')
  document.getElementById('right_transition_div')?.classList.add('transition_inactive')

  var leftTransitionDiv = document.getElementById('left_transition_div')
  if (leftTransitionDiv !== null) {
    leftTransitionDiv.style.height = '0%'
  }

  var rightTransitionDiv = document.getElementById('right_transition_div')
  if (rightTransitionDiv !== null) {
    rightTransitionDiv.style.height = '0%'
  }

  timeout_active = false
}

function postAnswer(vote: number): void {
  fetch(QUESTIONS_API, {
    method: 'POST',
    body: JSON.stringify({
      question_id: questions[question_counter]['ID'],
      vote_type: 'Votes' + String(vote)
    })
  })
}
</script>

<style>
@font-face {
  font-family: sheepFont;
  src: url(../assets/fonts/sheep.ttf);
}
.Myapp_question {
  width: 100%;
}

/*Holder image div set to hidden*/
#temp1,
#temp2 {
  display: none;
}

/* Center the header text vertically and horizontally */
#header_question {
  text-align: center;
  color: #a6cbce;
  position: absolute; /* Position the header absolutely within the .Myapp container */
  top: 12%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  z-index: 3; /* Ensure the header appears in front of the images */
  font-size: 44pt;
}

/* Create a flex container to hold the images side by side */
.image-container_question {
  display: flex;
  justify-content: space-between;
  height: 100vh;
  width: 200%;
  background-color: rgba(0, 0, 0, 1);
}

.container-transition-correct {
  transition: background-color 1s;
  background-color: rgb(51, 131, 43);
}

.container-transition-wrong {
  transition: background-color 1s;
  background-color: rgb(146, 33, 33);
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
  display: block;
  background-color: transparent;
  opacity: 0.5;
}

.imageLabel_question {
  color: #a6cbce;
  z-index: 3; /* Ensure the header appears in front of the images */
  position: absolute; /* Position the header absolutely within the .Myapp container */
  text-align: center;
  top: 75%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-size: 38pt;
  font-family: sheepFont;
}

.scoreLabel_question {
  color: #cc998d;
  z-index: 1; /* Ensure the header appears in front of the images */
  position: absolute; /* Position the header absolutely within the .Myapp container */
  text-align: center;
  top: 97%; /* Center vertically */
  left: 87%; /* Center horizontally */
  transform: translate(-50%, -50%); /*Center the header perfectly*/
  font-family: sheepFont;
  font-size: 26pt;
}

.transition_inactive {
  visibility: hidden;
  width: 50%;
  bottom: 0;
  left: 0;
  height: 0px;
  z-index: 2;
}

.transition_correct {
  width: 100%;
  background-color: rgba(47, 150, 38, 0.5);
  z-index: 2;
  bottom: 0px;
  height: 0px;
  position: absolute;
  transition: height 2s;
}

.transition_incorrect {
  width: 100%;
  background-color: rgba(182, 24, 24, 0.5);
  bottom: 0px;
  height: 0px;
  z-index: 2;
  position: absolute;
  transition: height 2s;
}

@media (max-width: 768px) {
  .Myapp_question {
    width: 100%;
  }

  /* Center the header text vertically and horizontally */
  #header_question {
    text-align: center;
    color: #a6cbce;
    position: absolute; /* Position the header absolutely within the .Myapp container */
    top: 50%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-family: sheepFont;
    z-index: 1; /* Ensure the header appears in front of the images */
    font-size: 22pt;
  }

  /* Create a flex container to hold the images side by side */
  .image-container_question {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100vh;
    width: 50vh;
    background-color: rgba(0, 0, 0, 1);
  }

  .container-transition-correct {
    transition: background-color 1s;
    background-color: rgb(51, 131, 43);
  }

  .container-transition-wrong {
    transition: background-color 1s;
    background-color: rgb(146, 33, 33);
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
    color: #a6cbce;
    z-index: 1; /* Ensure the header appears in front of the images */
    position: absolute; /* Position the header absolutely within the .Myapp container */
    text-align: center;
    top: 55%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-size: 18pt;
    font-family: sheepFont;
  }

  .scoreLabel_question {
    color: #cc998d;
    z-index: 1; /* Ensure the header appears in front of the images */
    position: absolute; /* Position the header absolutely within the .Myapp container */
    text-align: center;
    top: 94%; /* Center vertically */
    left: 76%; /* Center horizontally */
    transform: translate(-50%, -50%); /*Center the header perfectly*/
    font-family: sheepFont;
    font-size: 26pt;
  }
}
</style>
