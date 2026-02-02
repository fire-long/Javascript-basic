# fastapi를 사용해서 파이썬 to html(웹) 데이터 serving 하는 방법 배워보기
# fastapi: 파이썬 서버 만들도록 돕는 도구
# pip install fastapi

# ipynb -. py로 변환함. 지금은 필요 없음 ###########################
# pip install nbconvert                
# 만약 jupyter notebook 및 anaconda prompt에서 이 코드를 작성한다면
# 폴더 경로 이동 후 jupyter nbconvert --to script main.ipynb 실행
##################################################################

# pip install uvicorn
# 파이썬 .py 파일 수정할 때 바로바로 실행에 반여되도록 돕는 서버용 라이브러리

# CORS Policy(Cross Origin Resource Sharing)
# 서로 다른 url 주소 간의 데이터 공유는 기본적으로 막혀있다.
# 프로토콜 ~ ip주소 ~ 포트번호 : 서로 동일하면 무관, 하나라도 다르면 웹 정책에 따라서 접근을 허용하지 않음!

# CORS 정책을 허용하는 방법: 응답해주는 서버에서 어떤 요청 url만 접근 허용할건지 설정


# 1. 필요한 라이브러리 로딩하기
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import crawling

# 2. 우리가 실행시킬 서버용 app 생성
app = FastAPI()

# 특정 url에 대해서 CORS 정책 허용해주기
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://127.0.0.1:5500'], #html 파일만 특정해도 됨
    allow_methods = ['*'],
    allow_credentials = True #Access-Control-Allow-Origin header 에러에 대응하는 것!
)

# 3. app에 정보를 요청할 수 있는 경로 연결(라우팅)
# -> 해당하는 경로로 요청이 들어왔을 때 실행할 함수
@app.get("/test")
def test(senddata : str):
    # 데이터 받아올 때, 매개변수로 지정하는 방법이 있음
    # ※이 때, 전송한 데이터 key 값 == 매개변수명 
    print("체크")
    print(f"받아온 데이터:{senddata}")
    
    src = crawling.crawling_img(senddata)
    
    # 결과 반환 시 딕셔너리 구조 추천!
    # dictionary가 들어가면 JS console에서 자동으로 JSON으로 변환됨
    # return {"result": senddata+"님 환영합니다"} 
    return {"result": src} 

@app.get('/news')
def news(senddata : str):
    news = crawling.news_crawling(senddata)
    return {'news': news}

# 4. app -> ip 주소 할당, 고유의 port 번호 할당
# app.run(host='127.0.0.1', port = 9000)