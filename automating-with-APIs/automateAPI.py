import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
#parameters = {'upc': '0012993441012'} # barcode 1
parameters = {'upc': '073366118238'} # # barcode 1
# Also mention API Keys as a entry in parameters if API Keys are present

response = requests.get(baseUrl, params=parameters)
# REQUEST URL
print(response.url)

content = response.content
info = json.loads(content)
print(type(info))
# JSON Content
print(info)

# Parse through JSON
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)
