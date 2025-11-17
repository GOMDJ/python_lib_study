from pathlib import Path
import shutil
import os
shutil.copy("source.txt", "dest.txt")   #source.txt파일의 내용물 복사하여 dest.txt로 붙여넣기
shutil.copy2("source.txt", "dest.txt")  #메타데이터도 복사

shutil.copytree("src_folder", "dst_folder") #src폴더내용 전체 복사 후 dst폴더에 붙여넣기

shutil.move("old.txt", "new.txt")   #old.txt -> new.txt로 파일 이동, old.txt는 사라짐

#파일 삭제
Path("test.txt").unlink()   #path방식
os.remove("test.txt")   #os방식
#shutil은 파일 하나 삭제하는 함수가 없다.

#폴더 삭제
shutil.rmtree("folder") #폴더와 내용 전부 삭제
Path("folder").rmdir()  #빈 폴더만 삭제
