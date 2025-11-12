#데코레이터
"""
개념   
    def a():
    
    def b():
    가 있을 떄, @a가 def b():의 윗줄에 있으면
    @a
    def b():
    
    b의 리턴 값은 a의 매개변수가 된다.
    def a(b):가 된다
    
"""

#유형 1
def repeat(n):
    def decorator(func):  # decorator가 func 받음
        """
        *args : 튜플로 묶어 주는 거. name에 1,2,3 이렇게 들어왔을 때 그냥 하면 에러 나니까, 튜플로 하나로 묶어줌, args는 그냥 변수이름, 아무 이름이나 써도 됨
        **kwargs : 딕셔너리로 묶어 주는 거. name에 이름 : 철수, 나이 : 23 이런식으로 들어오면 에러나니까 딕셔너리로 하나로 묶어줌, kwargs는 그냥 변수 이름
                둘 다 인자로 사용 안됨. 특수 기능이어서 func()비어있는 거랑 같은데 값 받기 위해서 존재.
        """
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"안녕, {name}")

greet("철수")
"""
n에는 3이 들어가고, repeat함수가 가장 먼저 리턴하는 함수인 decorator 매개변수인 func가 greet의 값이 들어간다. 
func가 안녕, 철수를 출력하고 wrapper함수로 이동해서 안녕, 철수가 3번 반복됨. 
"""