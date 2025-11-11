"""
기본적인 클래스 선언
"""

#기본
class Video:
    def __init__(self, title, duration): #객체 초기화, 세팅해주는거. self가 있어야 외부에서 접근가능. 객체로 박아주기 때문에
        self.title = title
        self.duration = duration

    def get_info(self):
        return f"{self.title}, {self.duration}"
    
video1 = Video("영상1", 60) #self는 video1이 된다.
video2 = Video("영상2", 90) #self는 video2가 된다.

print(video1.get_info()) 
print(video2.title)

#응용 1
class VideoConfig:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps
        # pass : 그냥 통과하는거 
    def get_resolution(self):
        return f"{self.width}X{self.height}"
        

config = VideoConfig(1920, 1080, 30)

print(config.get_resolution())
print(config.fps)

#응용 2

"""
    리스트, 딕셔너리, 튜플, 스트링, json 받는거 헷갈려서 하는 메모
    
    1. 리스트
        생성    my_list = [1,2,3,"안녕"]
        접근    print(my_list[4])   #"안녕"
        수정    my_list[0] = 100    #[100,2,3,"안녕"]
        추가    my_list.append(200) #[100,2,3,"안녕",200]

    2. 딕셔너리
        생성    my_dict = {"name":"철수", "age":19}
        접근    print(my_dict["name"])  #"철수", 대괄호로 접근
        수정    my_dict["age"] = 24
        추가    my_dice["city"] = "서울"    #{"name": "철수", "age": 24, "city": "서울"}

    3.튜플
        생성    my_tuple = (1,2,3)
                my_tuple = 1,2,3
        접근    print(my_tuple[0])
        수정    불가능

    4.문자열
        생성    my_string = "안녕하세요"
        접근    print(my_string[0]) #"안"
        수정    불가
        슬라이싱    print(my_string[0:2])   #"안녕"

    5.json
        json은 문자열
        data = json.loads(json_string)  #json을 딕셔너리로 변환
        my_dict = {"name": "영희", "age": 22}
        json_string = json.dumps(ny_dict)   #딕셔너리를 문자열로 변환

    접근은 다 대괄호로 함
"""
class Scenario:
    def __init__(self, title, scenes):
        self.title = title
        self.scenes = scenes

    def get_total_duration(self):
        time = 0
        for scene in self.scenes:
            time += self.scene['duration']
        return time
    def get_script(self):
        words = ""
        for scene in self.scenes:
            words += self.scene['text']
        return words

scenario = Scenario("테스트 영상", [
    {"text": "안녕하세요", "duration": 3},
    {"text": "반갑습니다", "duration": 2}
])

print(scenario.get_total_duration())  # 5
print(scenario.get_script())  # "안녕하세요 반갑습니다"