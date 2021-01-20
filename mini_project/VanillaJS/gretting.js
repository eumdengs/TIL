const form = document.querySelector(".js-form"),
  input = document.querySelector("input"),
  greeting = document.querySelector(".js-greetings");
//querySelector는 찾은 것을 하나 가져온다

const USER_LS = "currentUser",
  SHOWING_CN = "showing";

function saveName(text) {
  localStorage.setItem(USER_LS, text);
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = input.value;
  paintGreeting(currentValue);
  saveName(currentValue);
}

function askFormName() {
  form.classList.add(SHOWING_CN);
  form.addEventListener("submit", handleSubmit);
}

function paintGreeting(text) {
  form.classList.remove(SHOWING_CN);
  greeting.classList.add(SHOWING_CN);
  greeting.innerText = `Hello ${text}`;
}

function loadName() {
  const currentUser = localStorage.getItem(USER_LS);
  if (currentUser === null) {
    //she is not
    askFormName();
  } else {
    //she is
    paintGreeting(currentUser);
  }
}

function init() {
  loadName();
}

init();
