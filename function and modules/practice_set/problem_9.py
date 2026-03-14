import requests

a = requests.get("http://api.github.com/")
print(a.json())
