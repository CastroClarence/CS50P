import requests
import sys

api_key = '011cb837881e22ce2edb2874fea2d3bc01cd30af14958ae70a2010465422bc9c'

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

