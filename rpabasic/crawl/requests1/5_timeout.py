import requests

url = "https://api.github.com/events"

res = requests.get(url, timeout=0.001)
print(res.text)
