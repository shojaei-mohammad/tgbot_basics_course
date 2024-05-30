import requests

URL = "http://api.open-notify.org/astros.json"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    for person in data.get("people"):
        print(f"Name: {person.get('name')} craft: {person.get('craft')}")
