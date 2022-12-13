"""
This module provides buy or sell signals for stocks.
"""
import time
from utility import get_symbols, mlog, get_signal

signals_list = []


def run():
    """Place holder docstring"""
    symbols = get_symbols(screener_country="turkey")
    for symbol in symbols["data"]:

        symbol = symbol["s"].split(":")[1]
        candle_list = [60]  # Represented in minutes
        for candle in candle_list:

            signal1 = []
            msg = f"Turkish Stocks Buy/Sell Signals from @tradingview - {candle} min candle\n\n"
            signal = round(get_signal("turkey", symbol, candle), 3)
            signal1.append(signal)
            msg += f"{symbol} {signal} : "

            mlog(symbol, f"{symbol}, {candle} minute candle. TradingView")
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
