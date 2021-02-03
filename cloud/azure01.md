Microsoft Lean AZ-900 과정 정리(무작위)

## 01. Azure Database

`빅데이터` : 대량의 데이터

대규모 데이터 세트를 처리하기 위한 오픈 소스 클러스터 기술의 개발

Microsoft Azure는 빅 데이터 및 분석 솔루션을 제공하는 광범위한 기술 및 서비스를 지원

(Azure Synapse Analytics, Azure HDInsight, Azure Databricks 및 Azure Data Lake Analytics)

**Azure Cosmos DB**는 SQL, MongoDB, Cassandra, Tables 및 Gremlin API를 지원

**Azure Database for MySQL**은 기존 LAMP 스택 애플리케이션을 위한 논리적인 선택

**Azure Synapse Analytics**는 대량의 데이터를 분석하기 위한 논리적인 선택

<br/>
<br/>

## 02. Azure Virtual Machines

**스케일 업** : 서버 자체를 증가시켜서 능력 향상. 수직 스케일이라고도 한다. (파워업같은거겠지)

**스케일 아웃** : 서버의 숫자를 늘려서 향상하는 방식. 수평 스케일. 

![](https://images.velog.io/images/gnobaaaar/post/ec372272-43c3-436d-98c6-a5489b6aa23e/%EC%8A%A4%EC%BC%80%EC%9D%BC.JPG)

<br/>

**Azure 컴퓨팅**은 클라우드 기반 어플리케이션을 실행하기 위한 주문형 컴퓨팅 서비스

VM(가상 머신을 실행하기 위한 다양한 서비스 존재)

- Azure Virtual Machines : 클라우드에서 가상 머신 생성. IaaS 제공.
- Azure Container Instances : 컨테이너를 배포, 관리할 수 있는 컴퓨팅 리소스
- Azure App Service
- Azure Functions(또는 ‘서버리스 컴퓨팅’) : 서비스 실행 코드에 이상적
<br/>

**Azure Virtual Machines**을 사용하여 클라우드에서 VM 생성

VM은 IaaS를 가상화된 서버 형식으로 제공하여 다양한 방법으로 사용가능

미리 구성된 이미지(템플릿-OS, 개발도구, 소프트웨어가 미리 포함)을 사용하여 생성 가능

<br/>

### VM 사용예시

- 개발 및 테스트
- 클라우드에서 어플리케이션 실행
- 데이터센터를 클라우드로 확장
- 재해

<br/>

### Azure Batch

수백, 수천 개의 가상머신으로 스케일링하여 **대규모 병령 및 고성능 컴퓨팅(HPC) 일괄 작업 가능**

<br/>
<br/>

## 03. 가상머신과 컨테이너

![](https://images.velog.io/images/gnobaaaar/post/15b23f96-09ed-4e57-a59d-d613969e9917/containers-vs-virtual-machines.jpg)

둘 모두 어플리케이션과 그 부산물들을 독립된 단위로 묶어, 격리, 어디서든 실행 가능하게 하는 것

가장 큰 차이는 설계의 접근법

**가상머신**은 하이퍼바이저가 여러 게스트 OS기반의 VM을 띄우고 실행. 각 VM마다 독립된 환경을 제공한다. 하이퍼바이저는 분배 등의 지원.

반면 **컨테이너**는 OS의 많은 자원을 컨테이너들끼리 공유한다. 덕분에 부팅이 짧고 컨테이너의 개수가 늘어나도 공간 차지가 적다. MSA(Microservice Architecture). 

<br/>

### Azure Container Instances

가상 머신을 관리하거나 추가 서비스를 채택하지 않고도 Azure에서 컨테이너를 실행하는 가장 빠르고 간단한 방법을 제공한다. 실행되는 컨테이너를 업로드 할 수 있는 PaaS 제공.

<br/>

### Azure Kubernetes Service

많은 컨터이너의 자동화, 관리, 상호 작용의 작업을 오케스트레이션이라고 하고 Azure Kubernetes Service는 분산형 아키텍처와 대량의 컨테이너가 있는 완벽한 컨테이너 용 오케스트레이션이다.

<br/>
<br/>

## 04. 쿠버네티스

쿠버네티스는 위에서의 컨테이너의 관리를 위한 오픈소스 플랫폼(by 구글)

컨테이너들을 적절하게 매니징하는 솔루션이다(나중에 깊이 들어가보자)

![](https://images.velog.io/images/gnobaaaar/post/ceb2bcd3-c281-4cdd-8c0a-e647e92d5e9c/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4.jpg)
- 확장성
- 유연성
- 이식성

<br/>
<br/>

## 05. 그외

**Azure App Service**

위에서의 어플리케이션 가상화하는 2가지 외에 **Azure App Service**에 배포하는 방법이 있다.

인프라 관리가 필요없는 PaaS 환경으로 원하는 프로그래밍 언어로 웹앱, 백그라운드 작업, 모바일 백 엔드 및 RESTful API를 빌드하고 호스트 가능하다.

<br/>

**Azure Functions**

예를 들어 긴 시간 후 어플리케이션이 특정 입력을 기다린 후에 처리하는 방식이라면 대기 시간에는 요금을 내지 않는 Azure Functions이 도움이 될 수 있다.

- **Azure Functions**: 함수는 거의 모든 최신 언어로 코드를 실행할 수 있다.
- **Azure Logic Apps**: 논리 앱은 웹 기반 디자이너에서 설계되며 코드를 작성하지 않고도 Azure 서비스에 의해 트리거된 논리를 실행할 수 있다.