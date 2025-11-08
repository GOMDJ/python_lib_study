import requests
import json

url = 'https://api.github.com/users/GOMDJ'
response = requests.get(url)
data = response.json()

with open('github_profile.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)    
    
with open('github_profile.json', 'r', encoding='utf-8') as f:
    r_data = json.load(f)

print(r_data)
print(f"name : {r_data['name']}")
print(f"login: {r_data['login']}")
