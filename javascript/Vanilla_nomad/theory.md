### 기초

**argument**

```javascript
function sayHello(name, age){
    return 'Hello ${name}' you are ${age} years old';
}
```

```javascript
const calculator = {
    plus: function(a,b){
        return a+b
    }
}
// calculator.plus(6,12)로 사용이 가능하다
```



### JS Dom Function

HTML은 어떻게 Javascript와 같이 사용

- id 선택은 `#` -> CSS
- class 선택은 `.` -> CSS

```javascript
const title = document.getElementById("title");
title.innerHTML = "title changed";
title.style.color = "red" //색상변경

const title = document.querySelector("#title");
//자식을 찾는다
```



### DOM(Document Object Module)

모든 html항목은 객체가 된다



### Event and Event handlers

자바스크립트는 이벤트

```javascript
function handle(event){
    console.log(event);
}
window.addEventListener("resize", 함수를 넣어준다=hadnle(event))
```

- 내가 필요한 시점에 함수를 호출한다
- 윈도우 사이즈를 변경할때 함수를 호출하자!

```javascript
function handleClick(){
    title.style.color = "red";
}
//title을 click하면 색상이 변경된다
title.addEventListener("click", handleClick);
```

```javascript
//마우스를 클릭하면 색상이 변경되는 타이틀 예제
const title = document.querySelector("#title");

const BASE_COLOR="red";
const OTHER_COLOR="blue";

function handleClick(){
    const currentColor = title.style.color;
    if (currentColor==BASE_COLOR){
        title.style.color = OTHER_COLOR;
    }
    else{
        title.style.color=BASE_COLOR;
    }
}

//초기화 함수
function init(){
    title.style.color = BASE_COLOR;
    title.addListener("click", handleClick);
}

init();
```



### If-Else Function Practice

**index.js**

```javascript
const title = document.querySelector("#title");

const CLICKED_CLASS = "clicked";

//현재 타이틀의 className은 공백상태
function handleClick(){
    const currentClass = title.className;
    if(currentClass !== CLICKED_CLASS){
        title.className = CLICKED_CLASS;
    }
    else{
        title.className = "";
    }
}


function init(){
    title.style.color = BASE_COLOR;
    title.addListener("click", handleClick);
}

init();
```

**index.css**

```css
body{
    background-color: #ecf0f1;
}

h1{
    color:navy;
    transition: color 0.5s ease-in-out;
}

.clicked{
    color:#7f8c8d;
}
```

**index.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Something</title>
        <link rel="stylesheet" href="index.css" />
    </head>
    <body>
        <h1 id="title">
            This works!
        </h1>
        <script src="index.js"></script>
    </body>
    
</html>
```





### More Function

**setInterval**

- setInterval(함수, milleseconds)

[javascript filter 함수에 대해 알아보자 자바스크립트 filter 함수 :: 알짜배기 프로그래머 (tistory.com)](https://aljjabaegi.tistory.com/312)

[자바스크립트 Array forEach (tistory.com)](https://yuddomack.tistory.com/entry/자바스크립트-Array-forEach)