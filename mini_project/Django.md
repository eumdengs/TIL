## Django

> 인프런+제코베



### 구현화면

**북마크구현**

![image-20210120112955833](images/image-20210120112955833.png)









**XD와 Zeplin을 사용하여 UI구성**

### 북마크 구현

**reset.css**

브라우저마다 기본값이 다르기에 모든 브라우저에서 통일된 화면을 보기위해서 기본값을 처음부터 초기화시킨다

```css
body
{
margin:0px;
padding:0px;
}
/*위와 같은 것을 쓰고 시작하는 것과 같다*/
```



**container 가운데 정렬**

```css
  position: absolute;
  left: 50%;
  top: 50%;
  /* 좌우 위아래의 - half */
  /* margin-left: -209px; */
  /* margin-top: -369.5px; */
  /*또는 아래와 같이 사용 */
  transform: translate(-50%, -50%);
```



태그는 블록, 인라인으로 나뉜다

블록은 밑으로 쌓이면서 영역의 좌우 전체를 가지게 된다 -> 따라서 width값이 필요가 없을 수 있다

**header**

```css
  height: 103px;
  background-color: #ff7063;
  font-size: 20px;
  font-weight: 500;
  font-style: normal;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  /* 메인축의 위치를 설정 */
  justify-content: center;
  /* 서브축의 위치를 설정 */
  align-items: center;
```

