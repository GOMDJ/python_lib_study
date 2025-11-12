import requests
import json

usernames = ['GOMDJ', 'smeteor0213', 'ysnam030213']
results = []

for username in usernames:
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results.append({
            'username' : username,
            'name' : data['name'],
            'followers' : data['followers'],
            'repos' : data['public_repos']
        })
    else:
        print(f"Failed to get {'username'} : {response.status_code}")
    
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"total users : {len(results)}")
