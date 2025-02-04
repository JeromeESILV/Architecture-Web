import requests

#projet perso
# Doc = https://waifu.im/docs/

#GET
api_url = "https://waifu.im/random/"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])