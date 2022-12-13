import datetime
from pprint import pprint
import requests
import json
from utility import dump_json


def mlog(market, *text):
    """Place holder docstring"""
    print(text)
    print(type(text))
    text = [str(i) for i in text]
    print(type(text))

    text = " ".join(text)

    datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

    print(f"[{datestamp} {market}] - {text}")

def test(test, arg="test"):
    """Place holder docstring"""
    print(test)
    print(arg)
    
    
def get_symbols(screener_country="turkey"):
    '''Place holder docstring'''

    headers = {"User-Agent": "Mozilla/5.0"}
    url = f'https://scanner.tradingview.com/{screener_country}/scan'
    symbol_lists = requests.post(url, headers=headers, timeout=10).json()
    dump_json(symbol_lists, "symbol_lists.json")
    data = symbol_lists["data"]
    return data

# json_data = get_symbols()

if __name__ == '__main__':
    get_symbols()
