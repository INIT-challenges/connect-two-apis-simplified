import requests
import json
response_API = requests.get('https://api.fungenerators.com/name/categories.json?start=0&limit=5')
# response_API = requests.get('https://api.fungenerators.com/name/generate?category=car&limit=1')
response_API = requests.get('https://randomuser.me/api/')

#print(response_API.status_code)

data = response_API.text

parse_json = json.loads(data)

print(parse_json)
