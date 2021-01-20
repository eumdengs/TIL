const toDoForm = document.querySelector(".js-toDoForm"),
  toDoInput = toDoForm.querySelector("input"),
  toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = "toDos";

//해야할일을 생성시 이곳에 생성
let toDos = [];

function deleteToDo(event) {
  //   console.dir(event.target);
  // 부모 요소를 찾을때 사용 가능한 console.dir
  const btn = event.target;
  const li = btn.parentNode;
  toDoList.removeChild(li);
  //   모든 아이템을 실행시켜 true인 아이템으로 array를 따로 만들어준다
  const cleanToDos = toDos.filter(function (toDo) {
    return toDo.id !== parseInt(li.id);
  });
  toDos = cleanToDos;
  saveToDos();
}

function saveToDos() {
  localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}

function paintToDo(text) {
  //   console.log(text);
  const li = document.createElement("li");
  const delBtn = document.createElement("button");
  const span = document.createElement("span");
  const newId = toDos.length + 1;
  delBtn.innerText = "❌"; //삭제버튼 형성
  delBtn.addEventListener("click", deleteToDo);
  span.innerText = text;
  //부모 엘리먼트에 넣기
  li.appendChild(delBtn);
  li.appendChild(span);
  li.id = newId;
  toDoList.appendChild(li);
  const toDoObj = {
    text: text,
    id: newId,
  };
  //push로 array에 삽입
  toDos.push(toDoObj);
  saveToDos();
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = toDoInput.value;
  paintToDo(currentValue);
  toDoInput.value = "";
}

function loadToDos() {
  const loadedToDos = localStorage.getItem(TODOS_LS);
  if (loadedToDos !== null) {
    const parsedToDos = JSON.parse(loadedToDos);
    // forEach를 통해서 내부 함수를 각각 실행해준다 => text형태로
    parsedToDos.forEach(function (toDo) {
      paintToDo(toDo.text);
    });
  }
}

function init() {
  loadToDos();
  toDoForm.addEventListener("submit", handleSubmit);
}

init();
