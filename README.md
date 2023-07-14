# 2023-Herethon-1

2023 여기톤 : HERETHON 1조

- **서비스 소개**

  ### **ANDO(안전한 도착, 안도)**

  _혼자 걷던 **여대생**의 불안한 거리를 **안도**하고 나의 **귀가친구**와 **안**전하게 **도**착할 수 있도록 , 저희 **ANDO**가 연결해드리겠습니다._

  **핵심기능**

  회원가입 시 학생증 이미지를 업로드한 여대생들만이 관리자에 의해 승인 가능

  - 작성자가 원하는 장소 , 수단으로 귀가 친구 모집 글 게시
  - 모집 글에 자유롭게 댓글을 작성하여 소통
  - 게시된 타인의 모집 글에서 귀가 친구 신청 후 참석
  - 참석 후 모집 완료 글에서 안전 귀가 인증 리뷰 작성

- **개발환경에서의 실행 방법**
    <aside>
    ⌨️ **install**
    
    </aside>
    
    - `pip install django==3.2.10`
    - `pip install pillow`
    - `pip install python-dotenv`
    
    <aside>
    ⌨️ **runserver**
    
    </aside>
    
    - `python manage.py runserver`
    
    <aside>

## ⚙️기술 스택

#### ✔️ 기획디자인

<img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">

#### ✔️ 프론트엔드

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

#### ✔️ 백엔드

<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

#### ✔️ 협업도구

<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">

## 😎팀원소개

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/SurfingLouis"><img src="https://avatars.githubusercontent.com/u/113294984?v=4" width="100px;" alt=""/><br /><sub><b>FE 팀장 : 이지현</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/pookey1104"><img src="https://avatars.githubusercontent.com/u/90364700?v=4" width="100px;" alt=""/><br /><sub><b>FE 팀원 : 김서윤</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/pjh402941"><img src="https://avatars.githubusercontent.com/u/104891747?v=4" width="100px;" alt=""/><br /><sub><b>FE 팀원 : 박주희</b></sub></a><br /></td>
     <tr/>
      <td align="center"><a href="https://github.com/kimjy01"><img src="https://avatars.githubusercontent.com/u/115777730?v=4" width="100px;" alt=""/><br /><sub><b>BE 팀원 : 김지연</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/fjqmqjrm"><img src="https://avatars.githubusercontent.com/u/126189239?v=4" width="100px;" alt=""/><br /><sub><b>BE 팀원 : 박서윤</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/y-won1209"><img src="https://avatars.githubusercontent.com/u/127853111?v=4" width="100px;" alt=""/><br /><sub><b>BE 팀원 : 심예원</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>

## 📂폴더 구조

```css

📂 2023-Herethon-1
└─ herethon1
 │
 ├─ 📂 herethon1
 │  ├─ __init__.py
 │  ├─ asgi.py
 │  ├─ settings.py
 │  ├─ urls.py
 │  └─ wsgi.py
 │
 ├─ 📂 account
 │  ├─ 📂 templates
 │  │   ├─ admin_page.html
 │  │   ├─ form_errors.html
 │  │   ├─ index.html
 │  │   ├─ login.html
 │  │   ├─ my_page.html
 │  │   ├─ my_page_update.html
 │  │   ├─ password_reset.html
 │  │   ├─ password_reset_complete.html
 │  │   ├─ password_reset_confirm.html
 │  │   ├─ password_reset_done.html
 │  │   ├─ password_reset_email.txt
 │  │   ├─ profile_page.html
 │  │   └─ signup.html
 │  │
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ forms.py
 │  ├─ models.py
 │  ├─ tests.py
 │  ├─ urls.py
 │  └─ views.py
 │
 ├─ 📂 boardapp
 │  ├─ 📂 templates
 │  │     └─ 📂 board
 │  │         ├─ board_detail.html
 │  │         ├─ board_list.html
 │  │         ├─ board_post.html
 │  │         ├─ comment_edit.html
 │  │         ├─ done_list.html
 │  │         └─ search.html
 │  │
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ forms.py
 │  ├─ models.py
 │  ├─ tests.py
 │  ├─ urls.py
 │  └─ views.py
 │
 ├─ 📂 image
 │
 ├─ 📂 profile
 │  └─ user.png
 │
 ├─ 📂 templates
 │  └─ base.html
 │
 ├─ .env
 │
 ├─ db.sqlite3
 │
 ├─ main.py
 │
 ├─ manage.py
 │
 └─ README.md

```
