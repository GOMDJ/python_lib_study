import requests
import json

url = 'https://api.github.com/users/GOMDJ'

try:
    response = requests.get(url, timeout = 5) #5초 타임아웃
    response.raise_for_status() #4xx, 5xx 에러 발생

    data = response.json()
    print(f"Success : {data['name']}")
except requests.exceptions.Timeout:
    print("Request timeout")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error : {e}")
except requests.exceptions.RequestException as e:
    print(f"Error {e}")

