# Django_ChatGPT_Project_BE
# Cardify
- 인증된 사용자가 각 주제 별로 암기하려는 항목을 입력하고 궁금한 내용은 챗봇에게 물어보면서 공부하는 서비스

## 목차

[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 환경](#2-개발-환경)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. 요구사항 시각화 및 데이터베이스 모델링(ERD)](#4-요구사항-시각화-및-데이터베이스-모델링(ERD))<br>
[5. UI](#5-UI)<br>
[6. 메인 기능](#6-메인-기능)<br>
[7. 추가 기능](#7-추가-기능)<br>
[8. 개발하며 경험한 오류와 해결방법](#8-개발하며-경험한-오류와-해결방법)<br>
<br>

## 1. 목표와 기능
### 1.1 목표
- 각 주제 별로 암기하려는 항목을 입력하고 궁금한 내용은 챗봇에게 물어보면서 공부하는 서비스
### 1.2 기능
- 인증된 사용자는 암기 항목을 작성할 수 있습니다.
- 암기 항목의 수정 및 삭제는 작성자만이 가능합니다.
- 챗봇에게 궁금한 내용을 물어보고 답변을 받을 수 있습니다.
<br>

## 2. 개발 환경 및 배포 Link 

### 2.1 개발 환경
#### [FrontEnd]  
<div>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
    <img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=Tailwind CSS&logoColor=white"/>
</div>

#### [BackEnd]
<div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
    <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>
</div>

#### [Tool]
<div>
    <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</div>
<br>

### 2.2 배포 Link
[Cardify](http://13.209.212.147/accounts/login.html)
> 테스트용 ID 및 PW  
> ID : guest1  
> PW : dhwjdqo1!  

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조
📦BE  
 ┣ 📂.git  
 ┣ 📂accounts  
 ┃ ┣ 📂migrations    
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂Cardify  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜asgi.py  
 ┃ ┣ 📜settings.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜wsgi.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂chatbot  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜throttles.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂media  
 ┃ ┗ 📜default_profile_image.png  
 ┣ 📂memorycards  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📂__pycache__  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜permissions.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜__init__.py  
 ┣ 📂static  
 ┣ 📂venv  
 ┣ 📜.env  
 ┣ 📜.gitignore  
 ┣ 📜db.sqlite3  
 ┣ 📜manage.py  
 ┣ 📜README.md  
 ┣ 📜requirements.txt  
 ┗ 📜secrets.json  

<br>

### 3.2 API 명세서
- accounts

|App|URL|HTTP Method|HTML File Name|Note|Login|Author|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|accounts|register/|POST|register.html|회원가입 화면|||
|accounts|login/|POST|login.html|로그인 화면|||
|accounts|profile/|GET|profile.html|프로필 화면|✔️||

- memorycards

|App|URL|HTTP Method|HTML File Name|Note|Login|Author|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|memorycards|/|GET|memory_card_list.html|글목록 화면|✔️||
|memorycards|/|POST|memory_card_list_write.html|글목록 화면|✔️||
|memorycards|<int:pk>/|GET|memory_card_content.html|상세글 화면|✔️||
|memorycards|<int:pk>/|PUT|memory_card_content_edit.html|글 수정 화면|✔️|✔️|
|memorycards|<int:pk>/|DELETE|memory_card_content.html|글 삭제|✔️|✔️|

- chatbot

|App|URL|HTTP Method|HTML File Name|Note|Login|Author|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|chatbot|/|GET|chat.html|이전 채팅 내용 확인|✔️|✔️|
|chatbot|/|POST|chat.html|챗봇에게 답변 요청|✔️|✔️|

### 3.3 개발 일정

<div align="center">
<img width="800" alt="NotionTimeline" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/d16445cd-8192-4494-acc6-794c837440a5"><br>
- 타임라인 -<br>
<br>

<img width="800" alt="WBS" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/f3ba8b42-8ffd-43d5-90d3-7385e5396cff"><br>
<img width="800" alt="WBS" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/61f956b3-5d98-4232-99b8-9bed5712bf37"><br>
<img width="800" alt="WBS" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/f1510bb6-1b7b-4916-87ec-3ff1da2cd775"><br>
[WBS 스프레드시트](https://docs.google.com/spreadsheets/d/e/2PACX-1vQbfMrsn7gFsPs00l8CcxiGUMpIx7_rD-jf7RDY5ekv6mSTFPnxom0IQa6QphAAhllef_RJMnMvh0Yq/pubhtml)
</div>
<br>

## 4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도
<div align="center">
<img width="800" alt="MindMap" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/2f014b9d-841d-4e58-b91b-6e17167a2768"><br>
    - 기능 요구사항(마인드맵) - <br>
<br>

<img width="800" alt="FlowChart" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/a18f572f-5656-4152-805c-2cd1f8630b0d"><br>
    - 플로우 차트 - <br>
<br>

<img width="800" alt="ERD" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/ecde53ea-9f7f-48d8-b971-1eaf0f3cfa32"><br>
    - 데이터베이스 모델링(ERD 설계) - <br>
<br>

<img width="800" alt="architecture" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/1e989e6a-2566-488e-a213-ba35ad8a708b"><br>
    - 배포 아키텍처 구성도 - <br>
<br>
</div>
<br>

## 5. UI
### 5.1. 와이어프레임
<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/28160bd1-efb4-410a-85fa-7fdc03ed2c81">

### 5.2. 실제 UI
- GitHub Link : [Django_ChatGPT_Project_FE](https://github.com/Alexmint001/Django_ChatGPT_Project_FE)

|||
|-|-|
|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/75d7dd92-ea97-4c0d-ae51-f4781daec151"><br><div align="center">01_로그인 페이지</div>|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/561a86f0-1541-4798-bab9-8a03ae4b513b"><br><div align="center">02_회원가입 페이지</div>|
|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/bb42a263-2771-4b94-b1c5-8bc1f8f15ce4"><br><div align="center">03_프로필 페이지</div>|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/7f5c5705-46a1-44f8-9ecc-38711116e26b"><br><div align="center">04_글 목록 페이지</div>|
|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/4ebf0912-4f72-43b7-bca2-b4d9a3c1b2d6"><br><div align="center">05_글 작성 페이지</div>|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/6a9bf372-81ca-4a6e-88cc-cf1d1f412780"><br><div align="center">06_작성자가 아닌 사용자가 보는 페이지</div>|
|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/d384c318-fb15-4ec6-8962-2bf9c024ea8d"><br><div align="center">07_작성자인 사용자가 보는 페이지</div>|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/a6156475-a8e2-4d61-9a1f-741fa77da912"><br><div align="center">08_글 수정 페이지</div>|
|<img width="450px" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/b75b0da3-c598-43ac-bd30-038684f36afe"><br><div align="center">09_챗봇 페이지</div>||

### 5.3. 기능 별 GIF

<div align="center">
    
|||
|-|-|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/5d677e35-17bf-4104-becf-5d7ef460842a">|<div align="center">회원가입 기능</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/8abcd43a-81aa-4f35-8673-02e10798e86c">|<div align="center">로그인 기능</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/27d1858e-4110-44e5-adc0-068a39daa169">|<div align="center">프로필 기능</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/98b2578f-919c-4895-adea-d3f2e7c11f8a">|<div align="center">로그아웃 기능</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/02282032-7522-4fa2-89a2-2704639a2ae7">|<div align="center">글 쓰기 및 글 읽기 기능 / CREATE, GET</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/10a991de-a814-4e74-a5fa-87d3423a3f0f">|<div align="center">글 수정 및 글 삭제 / PUT, DELETE</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/124f7d0c-99c5-4156-a52c-fcaa46b6475b">|<div align="center">챗봇 요청 및 답변 / POST, GET</div>|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/8f454c96-39ac-4270-af24-499fde234831">|<div align="center">챗봇 요청 횟수 초과</div>|

</div>
<br>

## 6. 메인 기능
### 6.1. DRF 글 작성/읽기/수정/삭제 기능 구현
- mermorycards
    - `ModelViewSet`을 상속받는 `MemoryCardViewSet`을 작성하여 CRUD 구현
    - 로그인한 사용자만 READ(GET), CREATE(POST) 가능하도록 `permission_classes`에 `IsAuthenticated` 설정
    - 작성자 본인일 경우에만 UPDATE(PUT), DELETE(DELETE) 가능하도록 `permissions.py`에 `IsAuthorOrReadOnly` 작성 후 설정
    - 소스 코드 링크 : [memorycards/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/memorycards/views.py#L8C1-L28C23) / [memorycards/permissions.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/memorycards/permissions.py#L4C1-L21C5) / [memorycards/serializers.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/memorycards/serializers.py#L4C1-L19C21)
### 6.2. DRF 로그인/회원가입 기능
- accounts
    - `GenericAPIView`를 상속받는 `LoginView`를 작성하여 로그인 구현 - POST
    - `CreateAPIView`를 상속받는 `RegisterView`를 작성하여 회원가입 구현 - POST
    - 소스 코드 링크 : [accounts/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/views.py#L11C1-L75C32) / [accounts/serializers.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/serializers.py#L7C1-L66C51)
### 6.3. OpenAI API 연결하여 챗봇 구현
- chatbot
    - `APIView`를 상속받는 `ChatBotView`를 작성하여 챗봇 구현 - GET / POST
    - 소스 코드 링크 : [chatbot/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/chatbot/views.py#L17C1-L60C64)
<br>

## 7. 추가 기능
### 7.1. DRF CRUD는 Jason Web Token 방식으로 적용
### 7.1.1. CREATE, READ - 인증된 사용자 (ACCESS TOKEN)
- memorycards
    - `Settings.py`의 `REST_FRAMEWORK` 의 `DEFAULT_AUTHENTICATION_CLASSES` 설정을 `rest_framework_simplejwt.authentication.JWTAuthentication`으로 설정하여 JWT 사용
    - `ModelViewSet`을 상속받는 `MemoryCardViewSet`의 `permission_classes`를 통해 인증된 사용자를 검증할 수 있습니다.
    - 소스 코드 링크 : [Cardify/settings.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/Cardify/settings.py#L150C1-L154C2) / [memorycards/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/memorycards/views.py#L8C1-L27C11)

### 7.1.2. UPDATE, DELETE - 인증된 사용자 (ACCESS TOKEN) + 작성자 본인 (author field)
- memorycards
    - `Settings.py`의 `REST_FRAMEWORK` 의 `DEFAULT_AUTHENTICATION_CLASSES` 설정을 `rest_framework_simplejwt.authentication.JWTAuthentication`으로 설정하여 JWT 사용
    - `ModelViewSet`을 상속받는 `MemoryCardViewSet`의 `permission_classes`를 통해 인증된 사용자를 검증할 수 있습니다.
    - `serializers.py`에서 `get_is_author` 메서드를 오버라이딩 하여 작성자 본인일 경우 True를 리턴합니다.
    - `permissions.py` 에서 GET 요청은 인증 여부와 상관없이 항상 True를 리턴하되 그 외 요청(PUT, DELETE)에 대해서는 작성자에게만 True를 리턴하도록 `has_object_permission` 메서드 오버라이딩
    - 소스 코드 링크 : [memorycards/serializers.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/memorycards/serializers.py#L15C1-L19C21) / [memorycards/permissions.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/memorycards/permissions.py#L13C2-L20C42)

### 7.2. DRF 로그인, 회원가입 시 Jason Web Token 발급
### 7.2.1. DRF 로그인
- accounts
    - 로그인은 POST 요청이므로 `GenericAPIView`를 상속받는 `LoginView`를 작성하고, post 메서드를 오버라이딩, 사용자 인증 후 access token과 refresh token을 리턴
    - 소스 코드 링크 : [accounts/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/accounts/views.py#L43C1-L75C32)
### 7.2.2. DRF 회원가입
- accounts
    - 회원가입은 POST 요청이므로 `CreateAPIView`를 상속받는 `RegisterView`를 작성하고, post 메서드를 오버라이딩, 회원 가입 후 access token과 refresh token을 리턴
    - 회원가입 시 username과 email은 필수로 입력이 필요하고, 중복이 불가능 하다라는 설정과 password1과 password2는 같아야하고 필수로 입력이 필요하다는 설정은 `serializers.py`에서 `required`와 `validators`를 설정하였습니다.
    - 소스 코드 링크 : [accounts/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/accounts/views.py#L11C1-L41C38) / [accounts/serializers.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/accounts/serializers.py#L7C1-L35C6)

### 7.3. 챗봇 추가 기능
### 7.3.1. 이전에 챗봇과 채팅한 내용은 본인만 확인 가능 - 채팅 내용 데이터 베이스 저장 + 채팅 사용자 본인(user field)
- chatbot
    - 채팅 내용 본인만 확인 기능은 `APIView`를 상속받는 `ChatBotView`에서 `get_queryset` 메서드에서 요청한 사용자를 확인하고, 해당 사용자의 채팅을 가져오는 get 메서드를 오버라이딩하여 구현하였습니다.
    - 채팅 내용 DB 저장 기능은 post메서드를 오버라이딩하여 사용자를 지정한 후 저장하도록 구현하였습니다.
    - 소스 코드 링크 : [chatbot/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/chatbot/views.py#L28C5-L58C61)
### 7.3.2. 챗봇에 요청할 수 있는 횟수는 1일 5회로 제한 - UserRateThrottle을 상속받아 ChatBotThrottle 구현
- chatbot
    - 요청 횟수 제한 기능은 `throttles.py`에서 `UserRateThrottle`을 상속받는 `ChatBotThrottle`에서 `rate`를 `5/day`로 설정 후 `allow_request` 메서드를 오버라이딩하여 post요청에 한해서만 적용하도록 설정하였습니다.
    - `views.py`에서 `throttles_classes`를 작성한 `ChatBotThrottle`로 설정
    - `throttles`를 따로 작성한 이유 : `settings.py`에서 `DEFAULT_THROTTLE_RATES`로 설정을 하면 모든 요청에 횟수 제한을 두게 되므로 단순히 이전 내용을 읽어오는 get요청도 포함되기 때문.
    - 소스 코드 링크 : [chatbot/throttles.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/chatbot/throttles.py#L3C1-L13C5) / [chatbot/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/8ee148dcea402a4b8008dc139ff86f729bafca60/chatbot/views.py#L25C4-L25C41)
<br>

## 8. 개발하며 경험한 오류와 해결방법
### 2023-11-23
### 8.1. 로그인 시 BackEnd 서버와 FrontEnd서버 연결 에러 (DRF 기본 토큰 방식)😲
- 에러
    - `HTTP 403 Forbidden, CSRF Failed: Origin checking failed - http://127.0.0.1:5500 does not match any trusted origins.`
- 원인
    - 토큰이 신뢰할 수 있는 위치랑 매치 되지 않아서 생기는 에러
- 해결방법
    - `settings.py`에 기본 인증 클래스를 `TokenAuthentication`으로 설정하였다
- 소스코드 링크 : [Cardify/Settings.py Link](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/Cardify/settings.py#L149C1-L154C2)
<details>
<summary>참고한 django-rest-framework 소스 코드 authentication.TokenAuthentication 부분</summary>
<div markdown="1">

```python
...생략...

class TokenAuthentication(BaseAuthentication):
    """
    간단한 토큰 기반 인증입니다.
    클라이언트는 "Authorization"에서 토큰 키를 전달하여 인증해야 합니다
    문자열 "Token"으로 앞에 붙는 HTTP 헤더입니다. 
    예를 들어: Authorization: Token {token}
    """

    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token

    """
    사용자 지정 토큰 모델을 사용할 수 있지만 다음 속성이 있어야 합니다.
    * key -- 토큰을 식별하는 문자열입니다
    * 사용자 - 토큰이 속한 사용자
    """

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword

...생략...
```

</div>
</details>
<br>

### 2023-11-24
### 8.2. 클라이언트의 작성 페이지에서 작성 요청, 자격이 없다, 400 에러가 발생😲
- 에러
    - 클라이언트의 작성 페이지에서 제목과 내용을 작성 후 로컬저장소의 토큰을 getitem으로 담아서 요청, 자격이 없다, 400 에러가 발생
- 원인
    - author를 입력받아야 해당 글의 author를 지정하는데 클라이언트로 입력 받지 못하여 생긴 에러
- 해결방법
    - `serializers.py`에 `author`를 `ReadOnlyField`로 설정하였고, `views.py`에 `CreateModelMixin`의 `perform_create`를 오버라이딩 하여 기본적으로 `request.user`를 통해 자동적으로 설정되고. 이를 통해 `author`는 클라이언트로 부터 입력을 받지 않고, 서버에서만 수정이 가능하도록 하였다.
- 소스코드 링크 : [memorycards/Serializers.py Link](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/memorycards/serializers.py#L4C1-L19C21) / [memorycards/Views.py Link](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/memorycards/views.py#L8C1-L29C5)

### 2023-11-25
### 8.3. register(회원가입)에서 닉네임 추가 후 회원가입 시 발생한 에러😩
- 에러
  - `FieldError at /accounts/register/, Cannot resolve keyword 'nickname' into field.
    Choices are: auth_token, carduser, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser,
    last_login, last_name, logentry, memorycard, password, user_permissions, username`
- 원인
  - 기본 `User Model`에 `nickname field`가 없어서 발생한 오류
- 해결방법
  - `User`의 `AbstractUser`를 상속받아 커스텀 유저를 만들어서 해결해야함. `User Model`을 건드려야 하므로 초기에 진행했어야 함.
- 아쉬운 점
  - 이미 어느 정도 프로젝트가 진행이 된 상태라 `User Model` 커스텀 하기에는 부담이 되어 이 부분은 작업하지 못함.<br>
- 소스코드 링크 : [accounts/Models.py Link](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/models.py#L4C1-L15C47)

