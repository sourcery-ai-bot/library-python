import json
import requests

url = "https://restcountries-v1.p.rapidapi.com/all"

headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "c7ad4ca6b7msha4a35f57fe94fd1p1f7c60jsndbe42493472f"
}

response = requests.request("GET", url, headers=headers)

parsed = json.load(response.text)

print(parsed.dumps, indent=2)
