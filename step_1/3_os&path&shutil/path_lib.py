# %%
from pathlib import Path
# %%
current = Path.cwd() #current dir
print(current)

home = Path.home() #home dir
print(home)

file_path = Path("data/users.json") #현재경로부터 data/users.json파일 찾는거임. 현재경로가 기준
print(file_path)

folder = Path("data")   #data폴더
file = folder / "users.json"    #file경로라 data/users.json으로 설정됨
print(file)
# %%
path = Path("/home/user/project/data/users.json")   # 경로가 /로 시작하면 절대경로(루트 디렉토리부터 시작)
print(path.name)    #users.json 
print(path.stem)    #users 
print(path.suffix)  #json 
print(path.parent)  #/home/user/project/data
print(path.parts)   #('/', 'home', 'user', 'project', 'data', 'users.json')
# %%
path = Path("data/users.json")

print(path.exists())    #존재하는지 확인
print(path.is_file())   #파일인지 확인
print(path.is_dir())    #디렉토린지 확인
#%%
folder_1 = Path("logs")
folder_1.mkdir(exist_ok=True) #폴더 생성, 이미 존재해도 에러 안남

folder_2 = Path("data/2025/11")
folder_2.mkdir(parents=True, exist_ok=True)   #부모폴더도 함께 생성
folder_1.rmdir()    #정상 삭제
#folder_2.rmdir()    #rmdir은 빈 폴더만 삭제가능, 오류발생, 부모까지 삭제하고싶으면 shutil라이브러리 사용해야함
# %%
file_1 = Path("test_1.txt")
file.write_text("make file test", encoding = "utf-8")   #파일 쓰기
content = file.read_text(encoding="utf-8")  #파일 읽기
print(content)
# %%

file_2 = Path("test_2.txt")
file_2.write_bytes(b"binary test")    #바이너리 쓰기
data = file_2.read_bytes()    #바이너리 읽기
print(data)

# 일반 쓰기, 바이너리 쓰기 차이점
    # 텍스트로 쓰기 : utf-8 바이트로 인코딩해서 저장, 줄바꿈에 따라 os가 자동 변환될 수 있음
    # 바이너리 쓰기 : 날것의 바이트 데이터를 그대로 저장, 인코딩 변환 없음, 줄바꿈 변환 없음
                # 바이너리 : 컴퓨터가 이해하는 날 것의 데이터
                # 바이너리가 필요한 경우 : 이미지, 압축, 실행파일, 암호화된 데이터, 네트워크 프로토콜 데이터
# %%
folder = Path(".")  #현재 작업 디렉토리
for item in folder.iterdir():   #iterdir : iterate directory의 약자, 
                                #해당 폴더의 바로 아래 항목들만 반환(파일 + 폴더), 하위 폴더 안은 안 들어감
    print(item)
    
for py_file in folder.glob("*.py"): #glob : globbing pattern, 해당 폴더의 바로 아래 항목들만 반환(파일+폴더)
    print(py_file)
    
for py_file in folder.rglob("*.py"):    #rglob : recursive glob, 해당폴더의 모든 하위 폴더들 반환(파일+폴더)
    print(py_file)
# %%
