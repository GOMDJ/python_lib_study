# defaultdict : 키 없어도 에러 안나는 딕셔너리
# Counter : 개수 새기
# deque : 양쪽에서 추가/삭제 빠른 리스트, 이걸로 스택, 큐 구현 가능. 근데 스택은 리스트로 하는게 제일 좋음
# namedtuple : 이름으로 접근 가능한 튜플

from collections import defaultdict, Counter, deque, namedtuple

def keyerror_dict():    #키 값이 비어있을 때 발생하는 에러 예시
    word_count = {}

    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

    for word in words:
        word_count[word] = word_count[word]+1 

def common_answer():    #키 값이 비어있을 때 발생하는 일반적인 에러 해결법
    word_count = {}

    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] = word_count[word]+1 
        
    print(word_count)

def use_defualtdict():
    word_count = defaultdict(int)   #기본값으로 키에 0이 들어간다
    
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

    for word in words:
        word_count[word] += 1   #기본값으로 키에 0이 들어가기 때문에 에러가 발생하지 않는다
    
    print(dict(word_count)) #그냥 print(word_count)도 가능, json형식으로 저장할 때 저렇게 사용
    
#example 1 그룹화
def grouped():
    students = [
    {"name": "철수", "class": "A"},
    {"name": "영희", "class": "B"},
    {"name": "민수", "class": "A"},
    {"name": "지혜", "class": "B"},
    ]
    
    by_class = defaultdict(list)
    
    for student in students:
        by_class[student["class"]].append(student["name"])
        
    print(by_class)

def count():
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    count = Counter(words)
    
    print(count)    #각각 몇개인지
    print(count["apple"])   #apple의 개수 
    print(count.most_common(2)) #가장 많은거 2개

def str_count():
    text = "hello world"
    char_count = Counter(text)
    
    print(char_count)
    print(char_count.most_common(2))
    
def Dq():
    lst = [1, 2, 3]
    lst.insert(0, 0)    #O(n) 뒤에서부터 순차적으로하기 때문에
    lst.pop(0)  #O(n)
    
    dq = deque([1, 2, 3])
    dq.appendleft(0)    #맨 앞에(왼쪽)에 0 추가 O(1)
    dq.append(4)
    dq.popleft()    #O(1)
    dq.pop()

def Deque_ex():
    history = deque(maxlen = 3)
    history.append("command1")
    history.append("command2")
    history.append("command3")
    print(list(history))
    history.append("command4")    #이거 추가하면 자동으로 가장 오래된command1이 리스트에서 사라지고, 4가 추가됨.  
    print(list(history))
    
def named_tuple():
    #일반 튜플
    point_1 = (10, 20)
    print(point_1[0]) #인덱스로만 접근 가능
    #namedtuple, namedtuple는 클래스를 만들어주는 함수이다.
    point_2 = namedtuple("point_2", ["x", "y"])   #point_2 튜플에 이름을 달아줌
    p = point_2(40, 80) #p가 객체
    print(p.x)
    print(p.y)
    print(p[0])

def namedtuple_ex():
    Student = namedtuple("Student", ["name", "age", "grade"]) #첫번째 요소인 Student는 클래스명, 필드 이름을 리스트로 전달 
    s1 = Student("철수", 20, "A")   #객체 생성이 튜플로 만들어짐.
    s2 = Student("영희", 17, "B")
    
    print(s1.name)
    print(s2.age)   
    
def main():
    # grouped()
    # count()
    # Deque_ex()
    namedtuple_ex()
    
if __name__ == "__main__":
    main()
            
    


        
    