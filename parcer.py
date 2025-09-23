# import the library that processes HTTP requests
import requests

# create a dict that maps user provided cryptocurrency codes to API identifiers.
# for keys it has:
# 3-letter abbrevations or codes for cryptocurrency that a user inputs: "BTC", "ETH";
# for values it has:
# CoinGecko API identifiers: "bitcoin", "etherium"
crypto_ids = {'BTC': 'bitcoin', 'ETH': "etherium"}

# create a dict that maps crypto and currencies codes to normal names:
currency_id = {'BTC': 'Bitcoin', 'ETH': "Etherium", 'USD': 'US Dollar', 'EUR': 'Euro'}

# create a function that gets exchange rates:
# the function takes two parameters:
# "crypto" - a user entered crypto code (BTC, ETH)
# "currency" - a user entered currency code (USD, EUR).
# then it makes an http request and outputs the exchange rate.
def get_exchange_rate(crypto, currency):
    # the function will handle all (hopefully) mistakes so it starts with try:
    try:
        # validate the input:
        if not crypto and not currency:
            return {'error': 'Please, provide cryptocurrency and currency codes'}
        
        # create a viriable coin_id that gets CoinGecko identifier from the crypto_ids dict
        # after receiving the cryptocurrency code:
        coin_id = crypto_ids.get(crypto.upper())

        # build an API url for CoinGecko:
        url = f"https://api.coingecko.com//api/v3/simple/price?ids={coin_id}&vs_currencies={currency.lower()}"

        # make an HTTP request to the API and save the result in the variable "response":
        response = requests.get(url)

        # check if request was successful: if status is 200, it's ok, if other, raise error:
        response.raise_for_status()

        # convert the received json to python dict:
        data = response.json()

        # check if an API identifier is in the received data
        # and 
        # the user entered cryptocurrency code is in the received data
        if coin_id in data and currency.lower() in data[coin_id]:
            # get exchange rate:
            exchange_rate = data[coin_id][currency.lower()]
            crypto_name = currency_id.get(crypto.lower(), crypto)
            currency_name = currency_id.get(currency.lower(), currency)

            #return a dict with all information we can gather:
            return {'success': True,
                    'crypto_code': crypto,
                    'currency_code': currency,
                    'crypto_name': crypto_name,
                    'currency_name': currency_name,
                    'exchange_rate': exchange_rate,
                    'message': f"1 {crypto_name} = {exchange_rate:,.2f} {currency_name}"}
        else:
            return {'error': f"No data available for {crypto_name} / {currency_name}"}
    except requests.exceptions.RequestException as e:
        return {'error': f'Network error: {e}'}
    except Exception as e:
        return {'error': f"Unexpected error: {e}"}

# test
if __name__ == '__main__':
    print("=== Cryptocurrency Exchange Rate Parcer ===")
    test = [('BTC', 'USD'), ('?', 'EUR')]
    for crypto, currency in test:
        print(f"\nTesting {crypto} -> {currency}")
        result = get_exchange_rate(crypto, currency)
        if result.get('success'):
            print(f"Success: {result['message']}")
            print(f"Rate: {result['exchange_rate']}")
        else:
            print(f"Error: {result['error']}")