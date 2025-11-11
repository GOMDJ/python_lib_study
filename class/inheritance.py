"""
상속과 특수메서드를 다루는 파일
"""

import pathlib

class Animal:   #부모클래스
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):  #자식클래스
    def speak(self):
        return f"{self.name} : 멍멍"
    
class Cat(Animal):  #자식클래스
    def speak(self):
        return f"{self.name} : 야옹"
    
baduk = Dog("바둑이")
nabi = Cat("나비")

print(baduk.speak())
print(nabi.speak())

#응용 1
class MediaProcessor:
    def __init__(self, input_path):
        self.input_path = input_path
    
    def validate_file(self):
        return Path(self.input_path).exists()

# 자식1: 이미지 처리
class ImageProcessor(MediaProcessor):
    def resize(self, width, height):
        # 이미지 리사이즈
        pass

# 자식2: 오디오 처리
class AudioProcessor(MediaProcessor):
    def adjust_volume(self, level):
        # 볼륨 조절
        pass

# 둘 다 validate_file() 쓸 수 있음
img = ImageProcessor("image.jpg")
audio = AudioProcessor("audio.mp3")

img.validate_file()    # 부모 메서드
audio.validate_file()  # 부모 

#응용2 오버라이딩
#개념 : 부모함수와 자식함수의 이름이 같으면 자식함수를 사용한다. 
#1 init 오버라이딩
#핵심개념 : 인스턴스는 하나 밖에 존재하지않는다. 그래서 자식 인스턴스를 호출하면 부모 인스턴스를 불러오지 못한다. 그래서 super().__init__()를 해줘서 부모의 __init__함수 호출.
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal 생성")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  #super()은 부모를 가리킴 super().메서드() 부모의 메서드를 실행
        self.breed = breed       
        print("Dog 생성")

dog = Dog("바둑이", "진돗개")


print(dog.name)   # "바둑이" (부모에서 받음)
print(dog.breed)  # "진돗개" (자식에서 추가)

#2 메서드 오버라이딩
class Animal:
    def speak(self):
        print("동물이 소리낸다")

class Dog(Animal):
    def speak(self):  # 부모 메서드 덮어씀
        print("멍멍")

class Cat(Animal):
    def speak(self):  # 부모 메서드 덮어씀
        print("야옹")

dog = Dog("바둑이")
cat = Cat("나비")

dog.speak()  # "멍멍" (부모 거 안 쓰고 자기 거 씀)
cat.speak()  # "야옹"

#예제 1
class Generator:
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def save(self, filename, content):
        self.filename = filename
        self.filename = f"{content}.txt"
        path = f"{self.output_dir}/{filename}"
        with open(path, "w") as f:
            f.write(content)
        print(f"저장 완료 : {path}")

class VideoGenerator(Generator):
    def __init__(self, output_dir, fps):
        super().__init__(output_dir)
        self.fps = fps
    
    def generate(self, title):
        filename = f"{title}.txt" 
        self.save(filename, title)

video_gen = VideoGenerator("./output", 30)
video_gen.generate("영상1")

#특수 메서드
class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    # print() 했을 때 어떻게 보일지
    def __str__(self):
        return f"Video: {self.title} ({self.duration}초)"
    
    # len() 했을 때
    def __len__(self):
        return self.duration
    
    # + 연산자
    def __add__(self, other):
        return self.duration + other.duration

# 사용
video = Video("영상1", 60)
print(video)        # "Video: 영상1 (60초)"
print(len(video))   # 60

video2 = Video("영상2", 30)
print(video + video2)  # 90

#특수메서드
class Video:
    def __init__(self, title, duration):    #객체 초기화
        self.title = title
        self.duration = duration
    
    def __str__(self):  #자동으로 출력형식 지정
        return f"video : {self.title}, duration : {self.duration}"
    
    def __len__(self):  #len(video)하면 자동으로 duration길이 반환해줌
        return self.duration

    def __add__(self):  #video1+video2이렇게 해주면 자동으로 영상길이 더해줌
        return self.duration + self.duration
    

video1 = Video("제목", 20)

print(video1) #원래라면 제목, 20이 출력되어야하지만 __str__덕분에 video : 제목, duration : 20 이런식으로 출력됨
len(video1) #video1의 영상길이 반환 
    
"""
추가 메모

__의 의미
던더(dunder(double underscore))라고 부른다
파이썬이 쓰는 특별한 이름인데
    __name__    현재 모듈 이름
    __file__    현재 파일 경로
    __doc__     문서 문자열
    등을 나타낸다.
그리고 위의 특수 메서드에 사용된다.
if __name__ == "__main__":
    내용...

이게 왜 이 파일만 실행될 때 이 블록의 코드를 실행하라는 의미냐.
이 파일만 따로 실행하면 이 파일이 메인파일이 된다. 그래서 __name__가 __main__이 된다.
하지만 import해서 실행하게 되면 이 파일명이 __name__가 된다. 이걸 이용하여 적은거.
"""