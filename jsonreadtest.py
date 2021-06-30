import json

data = '{"results":[{"gender":"male","name":{"title":"Mr","first":"Vincent","last":"Walker"},"location":{"street":{"number":6294,"name":"Devonport Road"},"city":"Whangarei","state":"Taranaki","country":"New Zealand","postcode":61024,"coordinates":{"latitude":"66.9275","longitude":"-160.4003"},"timezone":{"offset":"+1:00","description":"Brussels, Copenhagen, Madrid, Paris"}},"email":"vincent.walker@example.com","login":{"uuid":"fd7a3fb9-be26-44c5-a6ad-463eabddc2ef","username":"redsnake329","password":"highheel","salt":"T4jxtVtA","md5":"932fd025163c8cfd6c253f0874c394da","sha1":"467ffc0ebf82fa89a4c37305c0c30161e06e8781","sha256":"de0520205b6bfdf43793585c4e1c323f6d64e6011388882a9993fdbd95eba688"},"dob":{"date":"1966-05-11T14:42:08.354Z","age":55},"registered":{"date":"2005-12-15T00:57:16.755Z","age":16},"phone":"(678)-871-9955","cell":"(118)-788-4647","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/93.jpg","medium":"https://randomuser.me/api/portraits/med/men/93.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/93.jpg"},"nat":"NZ"}],"info":{"seed":"0af1df326d3483b9","results":1,"page":1,"version":"1.3"}}'

parse_json = json.loads(data)

name = parse_json["results"][0]["name"]["title"] + " " + parse_json["results"][0]["name"]["first"] + " " + parse_json["results"][0]["name"]["last"]

print("Name: ", name)