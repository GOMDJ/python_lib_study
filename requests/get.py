import requests
url = 'https://api.github.com/users/GOMDJ'

response = requests.get(url)   #request라이브러리의 get()메서드로 url 가져오는 것을 response에 저장
print(response)
print(response.request)
"""
response.raise_for_status() #200이 아닌 경우 error
print(response.status_code)    #응답코드 불러오기
print(response.text)    #HTML코드 불러오기
print(response.json())  #json형식 딕셔너리로 파싱
"""
#특정 데이터만 불러오기
data = response.json()
print(f"Name : {data['name']}") 
print(f"login : {data['login']}")


