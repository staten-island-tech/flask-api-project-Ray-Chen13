import requests

response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
data = response.json()
print(data)  