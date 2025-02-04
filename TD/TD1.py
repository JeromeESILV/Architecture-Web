# Commande pour install requests :
# $ python -m pip install requests
# ou $ python -m pip install requests
import requests
import json 

#GET

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

response.status_code
response.headers["Content-Type"]


# POST
{
"userId": 1,
"title": "Buy milk",
"completed": 0
}


###

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()

response.status_code


#####


api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type":"application/json"} 
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.status_code

##PUT

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo) 
response.json()
response.status_code

#PATCH

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = response = requests.patch(api_url, {"title": "Mow lawn"}, json=todo) 
response.json()
response.status_code

#DELETE

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
response.json()
response.status_code

## https://github.com/public-apis/public-apis ##