# Permet de faire des requests
import requests

#API 1 AnimeFacts
#GET
api_url = "https://anime-facts-rest-api.herokuapp.com/api/v1"
response = requests.get(api_url)
print("-----------------------GET API n°1")
print(response.json())
print(response.status_code)


#API 2 Jikan
#GET
api_url = "https://api.jikan.moe/v4/anime/1"
response = requests.get(api_url)
print("-----------------------GET API n°2")
print(response.json())
print(response.status_code)


# API 3 AnimeNewsNetwork
#GET
api_url = "https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658"
response = requests.get(api_url)
print("-----------------------GET API n°3")
print(response.json())
print(response.status_code)


# API 4 AnimeChan
#GET
api_url = "https://animechan.vercel.app/api/quotes/"
response = requests.get(api_url)
print("-----------------------GET API n°4")
print(response.json())
print(response.status_code)