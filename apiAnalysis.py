import requests, json, time, datetime

def mlog(market, *text):
	text = [str(i) for i in text]
	text = " ".join(text)

	datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

	print("[{} {}] - {}".format(datestamp, market, text))

def get_symbols(screener_country):
	headers = {'User-Agent': 'Mozilla/5.0'}
	url = "https://scanner.tradingview.com/{}/scan".format(screener_country)
	symbol_lists = requests.post(url,headers=headers).json()
	data=symbol_lists["data"]
	return data

def get_signal(screener_country,market, candle):
	headers = {'User-Agent': 'Mozilla/5.0'}
	url = "https://scanner.tradingview.com/{}/scan".format(screener_country)

	payload =	{
					"symbols": {
						"tickers": ["BIST:{}".format(market)],
						"query": { "types": [] }
					},
					"columns": [
						"Recommend.Other|{}".format(candle),
						"Recommend.All|{}".format(candle),
						"Recommend.MA|{}".format(candle),
						"RSI|{}".format(candle),
						"RSI[1]|{}".format(candle),
						"Stoch.K|{}".format(candle),
						"Stoch.D|{}".format(candle),
						"Stoch.K[1]|{}".format(candle),
						"Stoch.D[1]|{}".format(candle),
						"CCI20|{}".format(candle),
						"CCI20[1]|{}".format(candle),
						"ADX|{}".format(candle),
						"ADX+DI|{}".format(candle),
						"ADX-DI|{}".format(candle),
						"ADX+DI[1]|{}".format(candle),
						"ADX-DI[1]|{}".format(candle),
						"AO|{}".format(candle),
						"AO[1]|{}".format(candle),
						"Mom|{}".format(candle),
						"Mom[1]|{}".format(candle),
						"MACD.macd|{}".format(candle),
						"MACD.signal|{}".format(candle),
						"Rec.Stoch.RSI|{}".format(candle),
						"Stoch.RSI.K|{}".format(candle),
						"Rec.WR|{}".format(candle),
						"W.R|{}".format(candle),
						"Rec.BBPower|{}".format(candle),
						"BBPower|{}".format(candle),
						"Rec.UO|{}".format(candle),
						"UO|{}".format(candle),
						"EMA10|{}".format(candle),
						"close|{}".format(candle),
						"SMA10|{}".format(candle),
						"EMA20|{}".format(candle),
						"SMA20|{}".format(candle),
						"EMA30|{}".format(candle),
						"SMA30|{}".format(candle),
						"EMA50|{}".format(candle),
						"SMA50|{}".format(candle),
						"EMA100|{}".format(candle),
						"SMA100|{}".format(candle),
						"EMA200|{}".format(candle),
						"SMA200|{}".format(candle),
						"Rec.Ichimoku|{}".format(candle),
						"Ichimoku.BLine|{}".format(candle),
						"Rec.VWMA|{}".format(candle),
						"VWMA|{}".format(candle),
						"Rec.HullMA9|{}".format(candle),
						"HullMA9|{}".format(candle),
						"Pivot.M.Classic.S3|{}".format(candle),
						"Pivot.M.Classic.S2|{}".format(candle),
						"Pivot.M.Classic.S1|{}".format(candle),
						"Pivot.M.Classic.Middle|{}".format(candle),
						"Pivot.M.Classic.R1|{}".format(candle),
						"Pivot.M.Classic.R2|{}".format(candle),
						"Pivot.M.Classic.R3|{}".format(candle),
						"Pivot.M.Fibonacci.S3|{}".format(candle),
						"Pivot.M.Fibonacci.S2|{}".format(candle),
						"Pivot.M.Fibonacci.S1|{}".format(candle),
						"Pivot.M.Fibonacci.Middle|{}".format(candle),
						"Pivot.M.Fibonacci.R1|{}".format(candle),
						"Pivot.M.Fibonacci.R2|{}".format(candle),
						"Pivot.M.Fibonacci.R3|{}".format(candle),
						"Pivot.M.Camarilla.S3|{}".format(candle),
						"Pivot.M.Camarilla.S2|{}".format(candle),
						"Pivot.M.Camarilla.S1|{}".format(candle),
						"Pivot.M.Camarilla.Middle|{}".format(candle),
						"Pivot.M.Camarilla.R1|{}".format(candle),
						"Pivot.M.Camarilla.R2|{}".format(candle),
						"Pivot.M.Camarilla.R3|{}".format(candle),
						"Pivot.M.Woodie.S3|{}".format(candle),
						"Pivot.M.Woodie.S2|{}".format(candle),
						"Pivot.M.Woodie.S1|{}".format(candle),
						"Pivot.M.Woodie.Middle|{}".format(candle),
						"Pivot.M.Woodie.R1|{}".format(candle),
						"Pivot.M.Woodie.R2|{}".format(candle),
						"Pivot.M.Woodie.R3|{}".format(candle),
						"Pivot.M.Demark.S1|{}".format(candle),
						"Pivot.M.Demark.Middle|{}".format(candle),
						"Pivot.M.Demark.R1|{}".format(candle)
					]
				}

    
	resp = requests.post(url,headers=headers,data=json.dumps(payload)).json()
	signal = oscillator = resp["data"][0]["d"][1]

	return signal


#get_signal("BTCUSDT", 60)
#get_signal("turkey","ERCB", 60)
signals_list = []
def run():
	screener_country="turkey"
	data=get_symbols(screener_country)
	for i in data:
		symbol =i["s"].split(":")[1]
		candle_list = [60] #Represented in minutes
		for candle in candle_list:
			signal1 = []
			msg = "Turkish Stocks Buy/Sell Signals from @tradingview - {} min candle\n\n".format(candle)
			mlog(symbol, "{}, {} minute candle. TradingView".format(symbol, candle))
			signal = round(get_signal(screener_country,symbol, candle),3)
			signal1.append(signal)
			msg += "{} {} : ".format(symbol, signal)
			if signal>0.5:
				msg+= "STRONG BUY\n"
				mlog(symbol, signal)
				signals_list.append(signal1)
				print("\n Signal List :",signals_list)
				print("\n Mesage :",msg)
				time.sleep(5)
			elif signal>0:
				msg+= "BUY\n"
			elif signal>-0.5:
				msg+= "SELL\n"
			else:
				msg+= "STRONG SELL\n"
			#mlog(symbol, signal)
		#signals_list.append(signal1)
		#print("\n Mesage :",msg)
		#print("\n Signal List :",signals_list)


if __name__ == "__main__":
    run()


