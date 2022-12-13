import datetime
from pprint import pprint
import requests
import json
from utility import get_signal_test, dump_json, mlog
from tradingview_ta import TA_Handler, Interval, Exchange


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

    tesla = TA_Handler(
    symbol="ETHUSDT",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_1_MINUTE
    )
    string = ""
    for key, value in tesla.get_analysis().summary.items():
        string += f"{key}: {value} "
    mlog("ETHUSDT", string)