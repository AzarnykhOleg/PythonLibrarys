import requests

url = "https://catfact.ninja/fact"

response = requests.get(url, verify=True)

if response.status_code == 200:
    print(response.text)
    print(response.json())
    print(response.url)
    print(response.headers)