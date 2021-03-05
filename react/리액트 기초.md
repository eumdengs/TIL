## React

<br/>

### 자바스크립트 기초

**function**

1. 함수는 리터럴에 의해 생성된다

2. 함수는 함수의 인자로 전달이 가능하다

3. 변수나 배열의 원소, 객체의 프로퍼티 등에 할당이 가능하다

4. 함수는 함수의 리턴값으로 리턴이 가능하다

5. 함수는 동적으로 프로퍼티를 생성 및 할당이 가능하다

<br/>

```
nodeJS` + `npm` + `npx
```

<br/>

npx설치

```jsx
npm install npx -g
```

npx를 이용하여 리액트 앱을 생성해준다

그리고 VSCode에서 실행

```
npx create-react-app movie_app
```

```
npm start
```

GitHub연동

<br/><br/>

### 간단한 컴포넌트

컴포넌트는 반환한다 -> html 함수

React 컴포넌트는 `render()`라는 메서드를 구현하는데, 이것은 데이터를 입력받아 화면에 표시할 내용을 반환하는 역할을 합니다. 이 예제에서는 XML과 유사한 문법인 JSX를 사용합니다. 컴포넌트로 전달된 데이터는 `render()` 안에서 `this.props`를 통해 접근할 수 있습니다.

<br/>

```react
class HelloMessage extends React.Component {
  render() {
    return (
      <div>
        Hello {this.props.name}
      </div>
    );
  }
}

ReactDOM.render(
  <HelloMessage name="Taylor" />,
  document.getElementById('hello-example')
);
```

<br/>

**React를 사용하기 위해서 JSX가 꼭 필요한 것은 아닙니다.** JSX를 컴파일한 JavaScript 코드를 확인하려면 **Babel REPL**을 이용

<br/><br/><br/>

React 는 사용자 인터페이스를 만들기 위한 컴포넌트 기반의 JavaScript 라이브러리

1. function으로 생성하는 방법 rsf
2. class로 생성하는 방법 rcc

<br/><br/><br/>

### React-hooks API 마스터

<br/>
먼저 React-hooks는 Function Component에서 사용가능하고, Lifecycle Method를 이용할 수 있는 최신 문법

즉 기존에 함수형 컴포넌트에서 못하던상태값 관리, 컴포넌트의 생명 주기 함수를 이용할 수 있게 되었다

<br/>

**리액트 property**

prop.fav = {fav}







### 비제어 컴포넌트

