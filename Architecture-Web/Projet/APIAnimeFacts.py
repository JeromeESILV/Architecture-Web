from asyncio import run_coroutine_threadsafe
import requests
import json 

#Doc = https://chandan-02.github.io/anime-facts-rest-api/
#home route = https://anime-facts-rest-api.herokuapp.com/api/v1
#specific route :
# v1/anime_name
# v1/anime_name/fact_id

#GET
api_url = "https://anime-facts-rest-api.herokuapp.com/api/v1"
response = requests.get(api_url)
##print fact
#print(response.json())

for data in response.json()["data"]:
    print("Anime : " , " ".join(data["anime_name"].split("_")))
    name = data["anime_name"]
    
    factData = requests.get(api_url + "/" + name).json()
    print("Trivia : ")
    for facts in factData["data"]:
        print(facts["fact"], "\n")
    print("################################\n")

print(response.status_code)
#print(response.headers["Content-Type"])