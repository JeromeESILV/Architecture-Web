import requests

# Doc = https://docs.api.jikan.moe
# https://api.jikan.moe/v4/anime/{id}

# GET
api_url = "https://api.jikan.moe/v4/anime/1"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])