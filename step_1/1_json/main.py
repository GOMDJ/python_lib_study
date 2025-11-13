#loads(string용 : string -> dict
#dumps(string용) : dict -> string
#load(파일용)
#dump(파일용)

import json

api_response = '''
{
  "status": "success",
  "data": {
    "users": [
      {"id": 1, "name": "철수"},
      {"id": 2, "name": "영희"}
    ]
  }
}
'''
data = {
    "name": "철수",
    "active": True,
    "score": None,
    "tags": ["python", "coding"]
}

response = json.loads(api_response)
print(response)

json_data = json.dumps(data)
print(json_data)

with open("user_1.json", "w", encoding = "utf-8")as f:
  json.dump(data, f, indent = 2, ensure_ascii=False)

with open("user_1.json", "r", encoding="utf-8") as f:
  loaded_data = json.load(f)

print(loaded_data)

name = response["data"]["users"][0]["id"]
print(name)