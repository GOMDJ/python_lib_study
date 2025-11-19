from pathlib import Path
from datetime import datetime
import shutil
import tempfile

def log_file():
    now = datetime.now()
    log_dir = Path("logs") / str(now.year) / str(now.month) / str(now.day)
    log_dir.mkdir(parents=True, exist_ok=True)
    # Path(f"logs/{now.year}/{now.month}/{now.day}").mkdir(parents=True, exist_ok=True), log_dir재사용안할 때 이렇게도 가능
    # Path("logs/2025/12/12").mkdir(parents=True, exist_ok=True), 경로 하드코딩할 때
    log_file = log_dir / f"app{now.strftime('%H%M%S')}.log"
    log_file.write_text("application started\n", encoding = "utf-8")

def find_extension():
    py_files = list(Path(".").glob("*.py")) #현재 경로의 py파일들을 py_files라는 리스트에 담음
    print(f"python file : {py_files}")
    for files in py_files:
        print(f"{files.name}")

def file_arrangement():
    source = Path(".")
    for file in source.iterdir():
        if file.is_file():
            ext = file.suffix[1:]
            if not ext:
                continue
            dest_folder = source / ext  #dest_folder = 현재 작업 디렉토리/확장자명
            dest_folder.mkdir(exist_ok=True)    #현재 작업디렉토리에 확장자명 폴더를 생성. 왜냐 dest_folder이 확장자명이기 때문에.

            shutil.move(str(file), str(dest_folder / file.name))    #file를 dest_folder(즉 py, json... 기타 등등)폴더로 이동
            print(f"{file.name} -> {ext}") #파일명이 ext폴더로 감.

def temp_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:  #delete=False를 왜 했냐. 
                                                                    # 원래 임시 파일로 생성되기 때문에 그냥 with구문이 끝나면 그냥 삭제가 된다. 
                                                                    # 하지만 뒤에 unlink를 보여줘야 하기 때문에 delete=False를 넣어서 삭제가 안되도록 함.
        f.write("temporary data")
        temp_path = f.name  #name은 사실 전체 경로를 반환. 따라서 변수명은 temp_path가 적절
    
    print(f"temp file : {temp_path}")

    Path(temp_path).unlink()    #파일 삭제

    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"temp dir : {tmpdir}")

def main():
    log_file()
        
if __name__ == "__main__":
    main()
    