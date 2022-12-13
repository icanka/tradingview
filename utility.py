"""
This module contains utility functions for the project.
"""
import json
import requests
import datetime


def get_symbols(screener_country="crypto"):
    '''Place holder docstring'''

    headers = {"User-Agent": "Mozilla/5.0"}
    url = f'https://scanner.tradingview.com/{screener_country}/scan'
    symbol_lists = requests.post(url, headers=headers, timeout=10).json()
    return symbol_lists


def mlog(market, *text):
    '''Log in a timed fassion'''
    text = [str(i) for i in text]
    text = " ".join(text)

    datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

    print(f"[{datestamp} {market}] - {text}")


def dump_json(data, filename):
    """Place holder docstring"""
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)


def get_signal(screener_country, market, candle):
    '''Place holder docstring'''
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://scanner.tradingview.com/{screener_country}/scan"

    payload = {
        "symbols": {"tickers": [f"BIST:{market}"], "query": {"types": []}},
        "columns": [
            f"Recommend.Other|{candle}",
            f"Recommend.All|{candle}",
            f"Recommend.MA|{candle}",
            f"RSI|{candle}",
            f"RSI[1]|{candle}",
            f"Stoch.K|{candle}",
            f"Stoch.D|{candle}",
            f"Stoch.K[1]|{candle}",
            f"Stoch.D[1]|{candle}",
            f"CCI20|{candle}",
            f"CCI20[1]|{candle}",
            f"ADX|{candle}",
            f"ADX+DI|{candle}",
            f"ADX-DI|{candle}",
            f"ADX+DI[1]|{candle}",
            f"ADX-DI[1]|{candle}",
            f"AO|{candle}",
            f"AO[1]|{candle}",
            f"Mom|{candle}",
            f"Mom[1]|{candle}",
            f"MACD.macd|{candle}",
            f"MACD.signal|{candle}",
            f"Rec.Stoch.RSI|{candle}",
            f"Stoch.RSI.K|{candle}",
            f"Rec.WR|{candle}",
            f"W.R|{candle}",
            f"Rec.BBPower|{candle}",
            f"BBPower|{candle}",
            f"Rec.UO|{candle}",
            f"UO|{candle}",
            f"EMA10|{candle}",
            f"close|{candle}",
            f"SMA10|{candle}",
            f"EMA20|{candle}",
            f"SMA20|{candle}",
            f"EMA30|{candle}",
            f"SMA30|{candle}",
            f"EMA50|{candle}",
            f"SMA50|{candle}",
            f"EMA100|{candle}",
            f"SMA100|{candle}",
            f"EMA200|{candle}",
            f"SMA200|{candle}",
            f"Rec.Ichimoku|{candle}",
            f"Ichimoku.BLine|{candle}",
            f"Rec.VWMA|{candle}",
            f"VWMA|{candle}",
            f"Rec.HullMA9|{candle}",
            f"HullMA9|{candle}",
            f"Pivot.M.Classic.S3|{candle}",
            f"Pivot.M.Classic.S2|{candle}",
            f"Pivot.M.Classic.S1|{candle}",
            f"Pivot.M.Classic.Middle|{candle}",
            f"Pivot.M.Classic.R1|{candle}",
            f"Pivot.M.Classic.R2|{candle}",
            f"Pivot.M.Classic.R3|{candle}",
            f"Pivot.M.Fibonacci.S3|{candle}",
            f"Pivot.M.Fibonacci.S2|{candle}",
            f"Pivot.M.Fibonacci.S1|{candle}",
            f"Pivot.M.Fibonacci.Middle|{candle}",
            f"Pivot.M.Fibonacci.R1|{candle}",
            f"Pivot.M.Fibonacci.R2|{candle}",
            f"Pivot.M.Fibonacci.R3|{candle}",
            f"Pivot.M.Camarilla.S3|{candle}",
            f"Pivot.M.Camarilla.S2|{candle}",
            f"Pivot.M.Camarilla.S1|{candle}",
            f"Pivot.M.Camarilla.Middle|{candle}",
            f"Pivot.M.Camarilla.R1|{candle}",
            f"Pivot.M.Camarilla.R2|{candle}",
            f"Pivot.M.Camarilla.R3|{candle}",
            f"Pivot.M.Woodie.S3|{candle}",
            f"Pivot.M.Woodie.S2|{candle}",
            f"Pivot.M.Woodie.S1|{candle}",
            f"Pivot.M.Woodie.Middle|{candle}",
            f"Pivot.M.Woodie.R1|{candle}",
            f"Pivot.M.Woodie.R2|{candle}",
            f"Pivot.M.Woodie.R3|{candle}",
            f"Pivot.M.Demark.S1|{candle}",
            f"Pivot.M.Demark.Middle|{candle}",
            f"Pivot.M.Demark.R1|{candle}",
        ],
    }

    resp = requests.post(url, headers=headers,
                         data=json.dumps(payload), timeout=10).json()
    signal = resp["data"][0]["d"][1]

    return signal
