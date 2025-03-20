
import requests


r = requests.get('https://dattebayo-api.onrender.com/characters')
data = r.json()
c = data["characters"]
print(c[0]["name"])

for personaj in c:
    print(f"Name - {personaj["name"]}")