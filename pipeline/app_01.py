import requests
from pprint import pprint

url = "https://api.coinbase.com/v2/prices/spot"

response = requests.get(url)

pprint(response.json())