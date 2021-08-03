# Web Application 제작

This is a very simple web application that shows results of survey from domestic traveller. And any traveller post their own trip on the page.

## TravNote
### 개요 
2020년 설문자료를 바탕으로 국내 여행에 대한 트렌드를 확인할 수 있고
자신의 여행을 기록할 수 있다.

### 구조
    Web_Application
    ├── flask_app
    │   ├── __pycache__
    │   ├── Data
    │   │   ├── codebook.pdf
    │   │   └── data_chart.py
    │   ├── models
    │   │   ├── db.survey_db
    │   │   └── survey.py
    │   ├── templates
    │   │   ├── index.html
    │   │   ├── create.html
    │   │   ├── trends.html
    │   │   ├── t_busan.html
    │   │   ├── recommend.html
    │   │   └── post.html
    │   ├── __init__.py
    │   ├── model.py
    │   └── routes.py
    ├── images
    │   └── chart
    │       └── .png
    │   └── .jpg
    ├── ERD.png
    ├── 2020_travel_survey.csv
    ├── model.pkl
    ├── requirements.txt
    ├── Procfile
    └── runtime.txt

### Service
#### Home
서비스의 목적 안내하고
Login, trends, post 등 중요 페이지로 이동 할 수 있다.

#### Trends
설문조사 데이터를 바탕으로 전체 데이터 추이를 확인할 수 있으며
도시별로 통계 추이를 확인할 수 있다.
여행 계획을 세우는데 참고하도록 하는 목적이 있었다.

#### Recommend
Trends에서 사용한 데이터를 바탕으로 
여행 예산/여행 지역에 대해 여행 출발 월을 추천해주는 프로그램을 만들고 싶었으나,
성공하지 못했다.

#### Post
촬영한 사진을 바탕으로 여행을 기록할 수 있다.


## 한계
모델링을 html상에 게재하지 못했다.
모델링 결과를 웹 상에서 확인 할 수 없다는 점이 아쉽다.
method=['GET', 'Post']를 제대로 익히지 못했다.
이 문제로 사용자의 입력 사항을 가져오거나 원하는 것을 웹으로 가져오는데 어려움이 생겼다.
결과적으로 모델링을 웹에서 확인하지 못했고, 사용자 계정에 대한 데이터를 주고받지 못했다.

추가로, 추후 업데이트 시 포스팅 페이지를 제작하고,
현제 이미지 파일로 게재된 데이터 통계 부분을
사용자들이 직접 원하는 대로 구현할 수 있도록 개선하면 좋겠다..
