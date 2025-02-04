
import requests
import json 

# https://animechan.vercel.app/api/quotes/

#GET
print("-----------------------GET")
api_url = "https://animechan.vercel.app/api/quotes/"
response = requests.get(api_url)
##print animes
for i in response.json():
    print("Title : ", i["anime"], "\n", "MC : ", i["character"], "\n","Quote from the Series : ",  i["quote"], "\n")

print(response.status_code, "\n")
#print(response.headers["Content-Type"], "\n")


# POST
print("-----------------------POST")
api_url = "https://animechan.vercel.app/api/quotes/"
todo = {
    'anime': 'Pandora hearts',
    'character': 'Oz Vessalius', 
    'quote': 'I was rejected, never given any expectations… Then at least, I won’t be a burden to others. It’s alright if the only one who hurts is me!'
}
response = requests.post(api_url, json=todo)
# print(response.json())

print(response.status_code)



