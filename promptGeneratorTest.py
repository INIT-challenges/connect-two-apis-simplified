import requests
import json

# response_API = requests.get('https://api.fungenerators.com/name/categories.json?start=0&limit=5')
# response_API = requests.get('https://api.fungenerators.com/name/generate?category=car&limit=10')

response_API = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/2/')
# ['destroy band indie', 'improvisational panpipe-step']

# response_API = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/story/2/')


#print(response_API.status_code)

data = response_API.text

parse_json = json.loads(data)

print(parse_json)
