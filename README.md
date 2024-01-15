# Django_ChatGPT_Project_BE
# Cardify
- 암기 카드를 작성하고 챗봇에게 물어보면서 공부하는 서비스

## 목차

[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 환경 및 배포 Link](#2-개발-환경-및-배포-Link)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. 요구사항 시각화, 데이터베이스 모델링(ERD), 배포 아키텍처 구성도](#4-요구사항-시각화,-데이터베이스-모델링(ERD),-배포-아키텍처-구성도)<br>
[5. UI](#5-UI)<br>
[6. 메인 기능](#6-메인-기능)<br>
[7. 추가 기능](#7-추가-기능)<br>
[8. 개발하며 경험한 오류와 해결방법](#8-개발하며-경험한-오류와-해결방법)<br>
<br>

## 1. 목표와 기능
### 1.1 목표
- 각 주제 별로 암기카드를 입력하고 궁금한 내용은 챗봇에게 물어보면서 공부하는 서비스
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

### ~~2.2 배포 Link~~<br>
**현재는 서버가 중지되어 있습니다.**<br>
~~[Cardify](http://13.209.212.147/accounts/login.html)~~
<details>
<summary>테스트용 ID 및 PW</summary>
<div markdown="1">
ID : guest1<br>
PW : dhwjdqo1!  
</div>
</details>

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
|memorycards|/|POST|memory_card_list_write.html|글 작성|✔️||
|memorycards|< int:pk >/|GET|memory_card_content.html|상세글 화면|✔️||
|memorycards|< int:pk >/|PUT|memory_card_content_edit.html|글 수정 화면|✔️|✔️|
|memorycards|< int:pk >/|DELETE|memory_card_content.html|글 삭제|✔️|✔️|

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

<img width="800" alt="WBS" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/ae5e30d7-040f-4d6c-bcf4-92744cb82ac9"><br>
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

<img width="800" alt="architecture" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/eb563c95-5ee1-40db-ab88-8c043ae4b0c4"><br>
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

## 6. 메인 기능

<div align="center">
    
|||
|-|-|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/5d677e35-17bf-4104-becf-5d7ef460842a">|**회원가입 기능**<br><br>`CreateAPIView`를 상속받는 `RegisterView`를 작성하여 회원가입 구현<br><br>**소스 코드 링크**<br>[accounts/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/views.py#L11C1-L75C32)<br>[accounts/serializers.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/serializers.py#L7C1-L66C51)|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/8abcd43a-81aa-4f35-8673-02e10798e86c">|**로그인 기능**<br><br>`GenericAPIView`를 상속받는 `LoginView`를 작성하여 로그인 구현<br><br>**소스 코드 링크**<br>[accounts/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/views.py#L11C1-L75C32)<br>[accounts/serializers.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/cee5d7a4c500f721dd74a1658402345752514826/accounts/serializers.py#L7C1-L66C51)|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/27d1858e-4110-44e5-adc0-068a39daa169">|**프로필 기능**<br><br>`GenericAPIView`를 상속받는 `ProfileView`를 작성하여 토큰 확인 후 프로필 화면에 출력할 데이터를 받아 프로필 화면 구현<br><br>**소스 코드 링크**<br>[accounts/views.py](https://github.com/Alexmint001/Django_ChatGPT_Project_BE/blob/76bd08cb3b4e286fed798931d694ca6c00b8853d/accounts/views.py#L77C1-L112C36)|
|<img width="450px" alt="" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/98b2578f-919c-4895-adea-d3f2e7c11f8a">|**로그아웃 기능**<br><br>로그아웃 버튼을 클릭 할 경우 로컬저장소의 토큰을 삭제하는 것으로 로그아웃을 구현<br><br>**소스 코드 링크**<br>[Django_ChatGPT_Project_FE/accounts/profile.html](https://github.com/Alexmint001/Django_ChatGPT_Project_FE/blob/e95798b62581d9c8eea88dab27876f691c514974/a텀
