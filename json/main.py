import json

"""
json.dumps : 딕셔너리 -> json형태로 변환
            왜 하냐, 딕셔너리는 파이썬만 읽을 수 있지만 json은 모든 언어 공통
"""
data = {'name' : 'john',
        'age' : '20'
        }

str_data = json.dumps(data)

print(data)
print(str_data)
print(type(data))
print(type(str_data))

