import requests
import sys

api_key = "secret"

bitcoins = sys.argv[1]

try:
    bitcoins = float(bitcoins)
    r = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}')
    data = r.json()["data"]
    bitcoin = float(data["priceUsd"])
except requests.RequestException:
    pass
except ValueError:
    pass

total = bitcoins * bitcoin
total = (float(total))
print(f"${total:,.4f}")

