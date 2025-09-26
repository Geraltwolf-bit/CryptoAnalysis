import requests

def validate_api(crypto, currency):
    url = "https://api.kraken.com/0/public/Ticker?pair={crypto}{currency}"
    response = requests.get(url)
    response.raise_for_status
    data = response.json()
    print(data)

validate_api('BTC', 'USD')