# Django_ChatGPT_Project_BE
# Cardify
- 인증된 사용자가 각 주제 별로 암기하려는 항목을 입력하고 궁금한 내용은 챗봇에게 물어보면서 공부하는 서비스

## 목차

[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 환경](#2-개발-환경)<br>
[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4. 데이터베이스 모델링(ERD)](#4-데이터베이스-모델링(ERD))<br>
[5. UI](#5-UI)<br>
[6. 메인 기능](#6-메인-기능)<br>
[7. 추가 기능](#7-추가-기능)<br>
[8. 개발하며 경험한 오류와 해결방법](#8-개발하며-경험한-오류와-해결방법)<br>

## 1. 목표와 기능
### 1.1 목표
- 각 주제 별로 암기하려는 항목을 입력하고 궁금한 내용은 챗봇에게 물어보면서 공부하는 서비스
### 1.2 기능
- 인증된 사용자는 암기 항목을 작성할 수 있습니다.
- 암기 항목의 수정 및 삭제는 작성자만이 가능합니다.
- 챗봇에게 궁금한 내용을 물어보고 답변을 받을 수 있습니다.

## 2. 개발 환경

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

### 3.2 URL 구조
- accounts

|App|URL|Views Function|HTML File Name|Note|
|:-------|:-----------|:-------------|:---------------------|:------------|
|accounts|'register/'|userregister|accounts/register.html|회원가입 화면 - POST 요청|
|accounts|'login/'|userlogin|accounts/login.html|로그인 화면 - POST 요청|
|accounts|'profile/'|userprofile|accounts/profile.html|프로필 화면 - GET 요청|

- memorycards

|App|URL|Views Function|HTML File Name|Note|
|:-------|:-----------|:-------------|:---------------------|:------------|
|memorycards|'/'|MemoryCardViewSet|memory_card/memory_card_list.html|글목록 화면 - GET 요청|
|memorycards|'/'|MemoryCardViewSet|memory_card/memory_card_list_write.html|글목록 화면 - POST 요청|
|memorycards|'${id}/'|MemoryCardViewSet|memory_card/memory_card_content.html|상세글 화면 - GET 요청|
|memorycards|'${id}/'|MemoryCardViewSet|memory_card/memory_card_content_edit.html|글 수정 화면 - PUT 요청|

- chatbot

|App|URL|Views Function|HTML File Name|Note|
|:-------|:-----------|:-------------|:---------------------|:------------|
|chatbot|'/'|ChatBotView|chat_bot/chat.html|챗봇 화면 - GET 요청 & POST 요청| 

### 3.3 개발 일정

<div align="center">
<img width="800" alt="NotionTimeline" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/d16445cd-8192-4494-acc6-794c837440a5"><br>
- 타임라인 -<br>
<br>

<img width="800" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/f3ba8b42-8ffd-43d5-90d3-7385e5396cff"><br>
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/61f956b3-5d98-4232-99b8-9bed5712bf37"><br>
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/f1510bb6-1b7b-4916-87ec-3ff1da2cd775"><br>
<a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vQbfMrsn7gFsPs00l8CcxiGUMpIx7_rD-jf7RDY5ekv6mSTFPnxom0IQa6QphAAhllef_RJMnMvh0Yq/pubhtml">WBS 스프레드시트</a>
</div>

## 4. 데이터베이스 모델링(ERD)
<div align="center">
<img width="800" alt="image" src="https://github.com/Alexmint001/Django_ChatGPT_Project_BE/assets/142385654/b917ce43-29f9-4bf9-8b2b-59663872d1c9"><br>
- 기능 요구사항(마인드맵) - <br>
<br>

<img width="800" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/9a2b6f7c-64c0-441b-8097-ad64f04b4a25"><br>
- 데이터베이스 모델링(ERD 설계)<br>
<a href="https://velog.io/@alexan1027/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%A7%81-%EA%B0%9C%EB%85%90-%EB%B0%8F-ERD-%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8-%EC%8A%A4%ED%84%B0%EB%94%94">ERD 블로그 정리</a>
</div>

## 5. UI
### 5-1. 와이어프레임
- [Mockup 테스트 페이지](https://ovenapp.io/view/RLB4pSeIPvYpCHhRChBNKNLbPwiuccir/6psTJ)    

|||
|-|-|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/d9d0cdc3-cb80-41a0-9b02-f7e224d5a346">01_메인페이지 - 로그인 전|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/41c2559b-d4c6-41f2-a4e6-c27f4c676c57">02_회원가입 페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/9ee28c98-44b2-4f2d-ac42-e3de627b50a0">03_프로필 페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/71b47345-72b3-479c-b75e-e7970d8739d9">04_메인페이지 - 로그인 후|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/b97dfc1d-8c68-42c2-978e-1855e4439b8e">05_카테고리 별 페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/cdd3b93c-c6c1-41fe-8b73-391f78ded4ec">06_콘텐츠 별 페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/8489a293-75ad-4d96-a700-6a447a6ddc3c">07_댓글 작성 시 페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/47bd4c0a-a2dc-477b-b8ec-033e5275c363">08_글 작성 시 페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/ad3e88e0-db38-4f1f-8024-1a9090772640">08_글 수정 시 페이지||

### 5-2. 실제 UI

|||
|-|-|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/d791421b-ee8a-4f3c-a77f-48dec984869a">01_메인페이지 - 로그인 전|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/f8c368ae-1aa2-4027-907d-1de0a5d02088">02_회원가입 페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/66ad9ddd-5daf-4357-9cb9-ba66647e9fc0">03_프로필 페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/7491d809-41ea-49da-a831-475f012dae99">04_메인페이지 - 로그인 후|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/740fc51f-78a0-400f-93f4-9d937b8b6456">05_블로그 입장|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/dd244027-c34e-4730-86d7-c1e7f00f8830">06_about페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/db446e43-2b46-4a45-afae-f1712b82c2b7">07_카테고리별페이지-1|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/93529fb7-b47e-487f-aeb5-034193b9b9bd">08_카테고리별페이지-2|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/6949b66d-1269-4cb6-a462-861f07dd750f">09_태그별페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/004eef28-0f1d-4cf7-8ed2-03ed72540763">10_콘텐츠별페이지|
|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/e6b34e41-ebae-4135-9c28-5a5d18437882">11_댓글작성페이지|<img width="100%" alt="image" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/d6be06d0-fc00-4a8b-91bf-30ded70a47f0">12_대댓글작성페이지|
|<img width="100%" alt="13_404Error페이지" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/780c2bd4-0bee-46f1-b2cf-b5661c7db2c5">13_404Error 페이지||

### 5-3. 기능 별 GIF

|||
|-|-|
|<img width="100%" alt="" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/3e30c1f3-48b3-4e0b-bc12-f49ea9ce5f8f">|메인페이지에서 회원가입 및 로그인을 하는 모습|
|<img width="100%" alt="" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/b970c89a-8ae1-47cc-9fbf-b43a7ff3b372">|메인페이지에서 블로그 진입과 게시글 작성하는 모습, <br>상세글 페이지에서 댓글 작성, 수정, 대댓글, 삭제가 되는 모습|
|<img width="100%" alt="" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/70e8938d-c6c9-4ed7-aaf1-c1a87e983249">|목록 페이지에서 게시글 수정 및 삭제가 되는 모습|
|<img width="100%" alt="" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/922df739-2bff-4bb5-81c1-60ae93b1ccd1">|카테고리 및 태그 별로 게시글 확인이 가능하며, 카테고리 및 태그 별로 검색이 가능합니다.|
|<img width="100%" alt="" src="https://github.com/Alexmint001/Django_Blog/assets/142385654/387408a6-2850-4652-82ee-143ba89e4f2b">|프로필 페이지에서 비밀번호 변경이 가능한 모습|

## 6. 메인 기능
### 블로그 CRUD 기능 구현
  - 게시글 작성 기능 
    - `PostCreateView(LoginRequiredMixin, CreateView)`로 구현

  - 게시글 수정 기능 
    - `PostUpdateView(UserPassesTestMixin, UpdateView)`로 구현

  - 게시글 삭제 기능
    - `PostDeleteView(UserPassesTestMixin, DeleteView)`로 구현

  - 게시글 검색 기능 ( 카테고리 및 태그에 따라 검색이 가능 )
    - 전체 글 검색 (`PostListView`에 구현하였습니다.)<br>
        <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/blog/views.py#L11C1-L25C24">`PostListView 소스코드 링크`</a>
    - 카테고리 별 검색 (`CategoryListView`에 구현하였습니다.)<br>
        <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/blog/views.py#L86C1-L107C23">`CategoryListView 소스코드 링크`</a>
    - 태그 별 검색 (`TagListView`에 구현하였습니다.)<br>
        <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/blog/views.py#L112C1-L133C23">`TagListView 소스코드 링크`</a>

### 로그인/회원가입 기능
  - 회원가입 기능 
    - `CreateView`로 구현
  - 로그인 기능 (로그인을 한 User만 게시글 작성, 수정, 삭제 가능)
    - `LoginView`로 로그인 기능 구현 후, `LoginRequiredMixin` 사용
  - 로그아웃 기능 
    - `LogoutView`로 로그아웃 기능 구현. `next_page`에 `accounts/login` 작성하여 로그아웃 후 로그인 페이지로 이동하도록 하였음. 
## 7. 추가 기능
  - 게시글 내 사진 업로드 (`models.py`에 `Imagefield` 추가)
  - 조회수 증가 (`models.py`에 `PositiveIntegerField` 추가)
  - 비밀번호 변경 기능
    - 함수형으로 구현<br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/accounts/views.py#L77C30-L77C30">`accounts/views.py 소스코드 링크`</a><br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/accounts/forms.py#L6C1-L14C29">`accounts/forms.py 소스코드 링크`</a><br>
  - 프로필 수정 기능
    - `ProfileUpdateView(View)`로 구현<br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/accounts/views.py#L14">`ProfileUpdateView 소스코드 링크`</a><br>
  - 닉네임 추가 기능
  - 댓글 추가
    - `CommentCreateView(LoginRequiredMixin, CreateView)`로 구현
  - 댓글 수정
    - `CommentUpdateView(UserPassesTestMixin, UpdateView)`로 구현
  - 댓글 삭제
    - `CommentDeleteView(UserPassesTestMixin, DeleteView)`로 구현
  - 대댓글
    - `ReCommentCreateView(LoginRequiredMixin, CreateView)`로 구현
  - 페이지네이션 기능 구현
    - `ListView`에 내장된 `paginate` 기능을 사용하였음.<br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/blog/views.py#L15C4-L17C20">`PostListView paginate 소스코드 링크`</a><br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/templates/blog/post_list.html#L42C32-L54C38">`paginate 적용 html 소스코드 링크`</a><br>
## 8. 개발하며 경험한 오류와 해결방법
- 2023.10.26
  - admin 페이지 깨지는 문제
  - 원인: 404Error 페이지 따로 만든다고 `settings.py`에서 `DEBUG` 설정을 `False`로 해놓은 것에서 문제가 발생한 것으로 확인
    - `DEBUG` 설정을 `False`로 놓으면 `Django`가 디버그 정보를 더이상 제공하지 않으며, 정적파일을 자동으로 제공하지 않음.
    - `Django`의 admin 페이지는 정적파일인 (JavaScript, CSS 등)을 사용하기 때문에 `DEBUG` 설정이 `False`인 상태에서 페이지가 깨지는 문제가 발생할 수 있습니다.
  - 해결방안
    - 정적 파일을 따로 제공하는 `collectstatic` 명령어를 사용하여 `STATIC_ROOT`에 지정된 위치로 복사하여 `DEBUG` 설정이 `FALSE` 이더라도 정적파일을 사용할 수 있도록 하여 해결하였음.
    - 추가로 `DEBUG=TRUE`는 개발할 때만 사용하는 설정이며, 배포 시에는 FALSE로 놓고, 정적파일 관리는 nginx 서버에서 하도록 설정해야한다.
- 2023.10.27
  - 카테고리 context 문제
    - 원인: `blog`의 `views.py`에서 `category.html`로만 `context`를 넘기는 것 때문에 `base.html`에서 해당 `context`를 받고 싶어도 받을 수 없었다.
  - 해결방안
    - `html`로 넘기고 싶은 `context`만 따로 utils폴더에 py파일로 만든 후 `settings.py`에 `context_procerssers`로 넘겨서 전체 파일에서 접근할 수 있도록 하였음.<br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/utils/context_processors.py#L1C1-L11C14">`utils/context_processors.py 소스코드 링크`</a><br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/firehelper/settings.py#L68C9-L76C15">`firehelper/settings.py 소스코드 링크`</a><br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/templates/base_detail.html#L22C9-L28C25">`templates/base_detail.py 소스코드링크`</a><br>
- 2023.10.30
  - 프로필 업데이트 기능 추가하다가 `405 Error` 발생
    ```
    Method Not Allowed (POST): /accounts/profile_update/
    Method Not Allowed: /accounts/profile_update/
    ```
  - 원인: `urls.py`에서 url 중복 관련으로 확인
  - 해결방안
    - 분명히 `ProfileUpdateView` 클래스를 구현하면서 `GET` 메소드랑 `POST` 메소드 둘다 작성을 해주었고, url 도 중복되지 않도록 작성하였다.
    - 이유를 찾다가 `views.py` 에서 `def post(self, request)` 라고 작성해야 할 것을 하나를 대문자로 `def Post(self, request)` 라고 작성해서 생긴 오류였다.
    - 즉, `Python`의 클래스 메서드는 대소문자를 구분하기 때문에 `post` 에 대한 기능이 없어서 허용되지 않은 메소드라고 출력한 것.
    - 단순한 오타로 발생한 오류이지만, 이를 계기로 더욱 꼼꼼하게 봐야겠다고 생각되었음.
- 2023.11.01
  - 댓글 수정 기능을 기존 함수형으로 구현했던 것을 클래스형으로 다시 구현하다가 `404 Error` 발생
  - 원인: 쿼리 결과에 `comment`가 없습니다.
    ```
    Request Method:POST
    Request URL:http://127.0.0.1:8000/blog/19/comment/edit/
    Raised by:blog.views.CommentUpdateView
    ```
    - `CommentUpdateView` 클래스를 구현하면서 `comment`를 수정하고, `post`의 pk값을 받는 것으로 구현하여 문제가 발생한 것으로 확인.
  - 해결방안
    - `models.py`에서 `comment`에 `post`를 외래키로 이미 구현을 해놓았기 때문에 `comment`의 `post`로 접근을 하고, `html`에서 `comment.pk`를 인자로 받도록 수정하여 해결하였음.<br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/blog/views.py#L156C1-L172C5">`CommentUpdateView 소스코드 링크`</a><br>
    <a href="https://github.com/Alexmint001/Django_Blog/blob/ed5527eaad667069368f25a2e4eef44f6dffb816/templates/blog/post_detail.html#L101C45-L106C52">`templates/blog/post_detail.html 댓글 수정 부분 소스코드 링크`</a><br>
- 2023.11.06
  - AWS lightsail 배포 후 정상적으로 실행되다가 `git pull`하고 나서 media 폴더를 로드하지 못하는 문제가 발생
  - 원인: nginx와 uwsgi 설정을 확인해본 결과 nginx 서버는 정상적으로 작동중인 것으로 확인을 하였고, uwsgi가 문제인 것으로 판단하였음.
```
[uwsgi]
chdir = /home/ubuntu/Django_Blog
module = firehelper.wsgi:application

uid = ubuntu
gid = ubuntu

#socket = /home/ubuntu/Django_Blog/Django_Blog.sock
socket=:8000
wsgi-file=/home/ubuntu/Django_Blog/firehelper/wsgi.py
callable=application
#chmod-socket = 664
check-static = /home/ubuntu/Django_Blog/
plugins=/usr/lib/uwsgi/plugins/python3_plugin.so

enable-threads = true
master = true
vacuum = true
pidfile = /home/ubuntu/Django_Blog/Django_Blog.pid
logto = log/uwsgi/@(exec://date +%%Y-%%m-%%d).log
log-reopen = true
static-map = /static=.static_root/
```
