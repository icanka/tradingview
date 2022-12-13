"""
This module provides buy or sell signals for stocks.
"""
import json
import time
import datetime
import requests
# make a request to pypi api


def mlog(market, *text):
    '''Log in a timed fassion'''
    text = [str(i) for i in text]
    text = " ".join(text)

    datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

    print(f"[{datestamp} {market}] - {text}")


def get_symbols(screener_country):
    '''Place holder docstring'''

    headers = {"User-Agent": "Mozilla/5.0"}
    url = f'https://scanner.tradingview.com/{screener_country}/scan'
    symbol_lists = requests.post(url, headers=headers, timeout=10).json()
    data = symbol_lists["data"]
    return data


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

    resp = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10).json()
    signal = resp["data"][0]["d"][1]

    return signal


# get_signal("BTCUSDT", 60)
# get_signal("turkey","ERCB", 60)
signals_list = []

def run():
    '''Place holder docstring'''
    screener_country = "turkey"
    data = get_symbols(screener_country)
    for i in data:
        symbol = i["s"].split(":")[1]
        candle_list = [60]  # Represented in minutes
        for candle in candle_list:
            signal1 = []
            msg = f"Turkish Stocks Buy/Sell Signals from @tradingview - {candle} min candle\n\n"
            mlog(symbol, f"{symbol}, {candle} minute candle. TradingView")
            signal = round(get_signal(screener_country, symbol, candle), 3)
            signal1.append(signal)
            msg += f"{symbol} {signal} : "
            if signal > 0.5:
                msg += "STRONG BUY\n"
                mlog(symbol, signal)
                signals_list.append(signal1)
                print("\n Signal List :", signals_list)
                print("\n Message :", msg)
                time.sleep(5)
            elif signal > 0:
                msg += "BUY\n"
            elif signal > -0.5:
                msg += "SELL\n"
            else:
                msg += "STRONG SELL\n"
            # mlog(symbol, signal)
        # signals_list.append(signal1)
        # print("\n Mesage :",msg)
        # print("\n Signal List :",signals_list)


if __name__ == "__main__":
    run()
