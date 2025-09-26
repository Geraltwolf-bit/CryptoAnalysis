import requests
import json

def test_url(api_url):
    print(f"Testing: {api_url}")
    response = requests.get(api_url)

    print(f"Status Code: {response.status_code}")
    print("Headers:", response.headers['content-type'])
    print("Response JSON:")
    print(json.dumps(response.json(), indent = 2))

test_url('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')