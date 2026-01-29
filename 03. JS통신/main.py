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

# 1. 필요한 라이브러리 로딩하기
from fastapi import FastAPI

# 2. 우리가 실행시킬 서버용 app 생성
app = FastAPI()

# 3. app에 정보를 요청할 수 있는 경로 연결(라우팅)
# -> 해당하는 경로로 요청이 들어왔을 때 실행할 함수
@app.get("/test")
def test():
    print("체크")
    print("체크2")
    return "반환하는 결과"

# 4. app -> ip 주소 할당, 고유의 port 번호 할당
# app.run(host='127.0.0.1', port = 9000)
