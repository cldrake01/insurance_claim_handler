import json
import requests
from dataclasses import dataclass, field

url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/alerts/%7Balert_id%7D"

payload = {
    "type": "stats_notification",
    "email_to": "example@test.com",
    "frequency": "daily"
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "a00c8b3566msh0f1b31a9a5eddd7p1edbf9jsn554e65b9b279",
    "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.request("PATCH", url, json=payload, headers=headers)

print(response.text)
