import requests

url = 'PUT_YOUR_URL_HERE'

response = requests.get(url)

print(response.json())