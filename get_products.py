import json
import requests
import statistics

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)
response_data = json.loads(response.text)
print (type(response_data))

for d in response_data:
    print("name: " + d["name"] + " id: " + str(d["id"]))