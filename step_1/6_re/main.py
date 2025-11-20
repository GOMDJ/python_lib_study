import re

def re_search():
    text = "my phone is 010-1234-5678"
    
    #찾기(search) - 첫번째 매칭
    match = re.search(r'\d{3}-\d{4}-\d{4}', text)
    if match:
        print(match.group())

def re_findall():
        #전부 찾기.
    text = "Number : 123, 456, 789"
    numbers = re.findall(r'\d+', text)  # 문자열 내에서 숫자 전부 찾아버리기. d+을 해서 연속해서 찾음.
    print(numbers)
    
def re_sub():
    #sub(치환)
    text = "Hello 123 World 456"
    result = re.sub(r'\d', 'X', text)  # d+를 x로 치환 -> hello X world X, d를 치환하면 hello XXX world XXX
    print(result)

def re_split():
    text = "apple,banana;cherry:grape"
    fruits = re.split(r'[,;:]', text)   # ,;:발견시 분리
    print(fruits)
    
def pattern():
    # \d - 숫자
    re.findall(r'\d', "abc123")  # ['1', '2', '3']
    re.findall(r'\d+', "abc123")  # ['123']

    # \w - 문자 (알파벳, 숫자, _)
    re.findall(r'\w+', "hello_world 123")  # ['hello_world', '123']

    # \s - 공백
    re.split(r'\s+', "a  b    c")  # ['a', 'b', 'c']

    # . - 임의의 문자 1개
    re.findall(r'a.c', "abc adc a c")  # ['abc', 'adc']

    # * - 0개 이상
    re.findall(r'ab*c', "ac abc abbc")  # ['ac', 'abc', 'abbc']

    # + - 1개 이상
    re.findall(r'ab+c', "ac abc abbc")  # ['abc', 'abbc']

    # ? - 0개 또는 1개
    re.findall(r'ab?c', "ac abc abbc")  # ['ac', 'abc']

    # [] - 문자 클래스
    re.findall(r'[aeiou]', "hello")  # ['e', 'o']

    # ^ - 시작
    re.match(r'^Hello', "Hello World")  # 매칭
    re.match(r'^World', "Hello World")  # None

    # $ - 끝
    re.search(r'World$', "Hello World")  # 매칭

def vaild_email():
    def is_vaild_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    print(is_vaild_email("test@gmail.com"))
    print(is_vaild_email("#gomdj@gmail"))
    
def main():
    # re_search()
    # re_findall()
    # re_sub()
    # re_split()
    vaild_email()

if __name__ == "__main__":
    main()
