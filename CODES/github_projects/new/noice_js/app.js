let userChosen;
let computerChosen;
let w = "You Won!";
let l = "You Lose!";
var result = results();
const displayResult = document.getElementById('result');
const computerChoice = document.getElementById('computer-choice');
const userChoice = document.getElementById('user-choice');
const possibleChoices = document.querySelectorAll('.choices');

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => { 
  userChosen = e.target.id;
  generateComputerChoice();
  results();
  userChoice.innerHTML = userChosen;
  computerChoice.innerHTML = computerChosen;
  displayResult.innerHTML = result;
}));

function generateComputerChoice() {
  
  const randomNumber = Math.round(Math.random() * (3))
  if (randomNumber === 1) {
    return computerChosen = "rock";
  } else if (randomNumber === 2) {
    return computerChosen = "paper";
  } else if (randomNumber === 3) {
    return computerChosen = "scissors";
  }
}


function results()  {
  if (computerChosen === userChosen) {
    return result = w;
  } else if (computerChosen === "rock" && userChosen === "paper") {
      return result = l;
  } else if (computerChosen === "rock" && userChosen === "scissors") {
      return result = w;
  } else if (computerChosen === "paper" && userChosen === "rock") {
      return result = l;
  } else if (computerChosen === "paper" && userChosen === "scissors") {
      return result = w;
  } else if (computerChosen === "scissors" && userChosen === "paper") {
      return result = l;
  } else if (computerChosen === "scissors" && userChosen === "rock") {
      return result = w;
  }





}
