import requests
import xml.etree.ElementTree as ET

# source = https://cdn.animenewsnetwork.com/encyclopedia/
# api.xml?anime=id
# api.xml?manga=id
# api.xml?title=id
# api.xml?anime=4658&manga=4199&manga=11608
# api.xml?anime=4658&manga=4199/11608
# api.xml?title=4658/4199/11608

#GET
api_url = "https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4240"
response = requests.get(api_url)
mytree = ET.parse(response.json())
myroot = mytree.getroot()
print(myroot)

#print(response.status_code)
#print(response.headers["Content-Type"])