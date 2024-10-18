# Django_study
Django 공부중 작성한 코드를 저장한 repository
## 🚩Django

### Django의 개발순서

1. Django프로젝트 생성
2. DB 초기화
3. 관리자 계정 만들기
4. App 만들기

1. 모델 설계하기(데이터베이스에 들어갈 데이터): 필드 = 모델의 칼럼

> 다음을 반복
> 
> 1. 뷰 만들기 
> 2. URL만들어서 보내기
> 3. 템플릿 만들기(HTML, CSS)

### **Django project, App**

**Django project생성하기**: `!django-admin startproject mysite`

생성한 프로젝트를 서버에서 실행하기: `python [manage.py](http://manage.py) runserver`

**Django App 생성하기**: ‘프로그래머스’라는 사이트(project) 안에 ‘커뮤니티’라는 부가기능 탭을 ‘App’이라고 부름
`python [manage.py](http://manage.py) startapp polls` → polls라는 이름의 앱을 생성해줌
1. mysite/urls.py에 urlpatterns를 수정해줌
2. polls/urls.py에 가서 polls/ 뒤에 path에 따라 어떻게 처리해줄 지 세팅해줌
3. polls/view.py에서 어떤 화면을 보여줄지 세팅해줌

### Django model

model: DB에서 데이터를 읽어와서 페이지에 보여줌. *ORM이라고도 부름*.

1. 모델을 생성
2. setting.py에 App을 등록해줌
3. 모델을 테이블에 써주기 위한 마이그레이션을 만듦
***Migration: model내 attribute에 변동사항 생기면 해줘야 함.***
    1. migration 파일 생성하기: `python [manage.py](http://manage.py) makemigrations polls`
    2. migration으로 실행될 SQL문장 살펴보기: `python [manage.py](http://manage.py) sqlmigrate polls 001`
    3. migration 실행하기: `python [manage.py](http://manage.py) migrate`
4. 이 모델에 맞는 테이블을 만듦
    1. sqlite에 들어가서 스키마 등을 확인: `sqlite3 db.sqlite3` 
        
        `.tables`: 테이블들 목록 확인
        
        `.schema 테이블명`: 테이블의 컬럼 확인
        
        `ctrl + D`: SQL 종료
        
    2. migration을 rollback: `python [manage.py](http://manage.py) migrate polls 0001`  → polls 0001로 롤백해라
        
        그 후, migrations 폴더에서 0002 삭제 & class에 칼럼 삭제 (ex.`score = models.IntegerField(default=0)`)
        

### Django admin

**polls/admin.py에서 모델 등록하기**
polls/models.py에서 생성된 질문 제목 설정
