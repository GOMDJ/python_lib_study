# %%
import os
# %%
print(os.environ.get("HOME"))   #HOME이라는 환경변수 가져오기 -> /Users/nam-yuseong
os.environ["MY_VAR"] = "value"  #MY_VAR이라는 환경변수 생성 후 value를 집어넣기
# %%
print(os.getcwd())  #현재 디렉토리
os.chdir("/tmp")    #현재 작업 디렉토리를 tmp로 변경
print(os.getcwd())
# %%
path = os.path.join("data", "users.json")   #옛날 방식 경로결합 -> data/users.json
print(path)
# %%
print(os.path.exists("data"))   #현재 폴더에서 data란 폴더가 존재하는지 
print(os.path.isfile("users.json")) #현재 폴더에 users.json이 파일인지 확인, users.json이 파일이 아니거나, 존재하지않으면 false반환
print(os.path.isdir("data"))    #현재 폴더에 data가 폴더인지 확인, data폴더가 없어도, 폴더가 아니어도 false반환
# %%
