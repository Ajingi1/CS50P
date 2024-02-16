import json
import requests
import sys
from sys import argv
try:
    if len(sys.argv) != 2:
        sys.exit("Missing Command-line argument")

    try:
        btc = float(sys.argv[1])

        resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        resp_json = resp.json()
        rate = resp_json["bpi"]["USD"]["rate_float"]
        print(f"${btc * rate:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
except requests.RequestException:
    ...
