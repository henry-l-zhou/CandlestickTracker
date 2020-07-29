from Candlesticks.Candlestick import Candlestick
#black == red, white == green
# open, close, low, high


def isLongGreenCandle(candlestick): # bullish signal
	open, close, low, high = candlestick.getProperties();
	return (close > open and ((close - open)/(.001 + high - low) > .6))

def isLongRedCandle(candlestick): # bearish signal
	open, close, low, high = candlestick.getProperties();

	return (open > close and ((open - close)/(.001 + high - low) > .6))
		
def isGreenMarubozu(candlestick): # bullish signal
	open, close, low, high = candlestick.getProperties();

	return ((close > open) and (high == close) and (open == low))

def isRedMarubozu(candlestick): # bearish signal
	open, close, low, high = candlestick.getProperties();

	return ((close < open) and (low == close) and (open == high))

def isDoji(candlestick): # neutral / reversal
	open, close, low, high = candlestick.getProperties();
	return (abs(open - close) <= ((high - low) *.1))

def isDragonflyDoji(candlestick): # bearish signal
	open, close, low, high = candlestick.getProperties();

	return ((high - low) > 3 * abs(open - close)) and ((close - low) > .8 * (high-low)) and ((open - low) > .8*(high - low))

def isGravestoneDoji(candlestick): #bullish signal
	open, close, low, high = candlestick.getProperties();

	return ((high - low) > 3 * abs(open - close)) and close <= (low + ((high-low) * .2)) and open <= (low + ((high - low)) *.2) 


def isHammer(candlestick1,candlestick2,candlestick3): # bullish signal
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return (open1 > open2) and (close1 > close2) and (open1 > close1) and (open2 > close2) and isDragonflyDoji(candlestick3)

def isInvertedHammer(candlestick1,candlestick2,candlestick3): # bearish signal
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return (open1 > open2) and (close1 > close2) and (open1 > close1) and (open2 > close2) and isGravestoneDoji(candlestick3)

def isBullishEngulfing(candlestick1, candlestick2):
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	

	return (open1 > close1) and (open2 < close1) and (close2 > open1) and (close2 > open2)

def isBearishEngulfing(candlestick1, candlestick2):
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();

	return (open1 < close1) and (open2 > close1) and (close2 < open1) and (close2 < open2)


def isBullishBeltHold(candlestick1, candlestick2, candlestick3): # bullish signal
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return ((close1 > open2) and (open1 >	 close1) and (open2 > close2) and (close2 > open3) and open3 < close3 and close2 < close3)

def isBearishBeltHold(candlestick1, candlestick2, candlestick3): # bullish signal
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return ((close1 < open2) and (open1 < close1) and (open2 < close2) and (close2 < open3) and open3 > close3 and close2 > close3)


# ((C1 < O1) AND (((O1 + C1) / 2) < C) AND (O < C) AND (O < C1) AND (C < O1) AND ((C – O) / (.001 + (H – L)) > 0.6))
def isPiercingLine(candlestick1,candlestick2,candlestick3): # bullish
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return (open1 > open2) and (close1 > close2) and (open1 > close1) and (open2 > close2) and ((open2 + close2) / 2 < close3) and (
		open3 < close3) and (open3 < close2) and (close3 < open2) and ((close3 - open3) / (.001 + (high3 - low3)) > .6)

def isDarkCloud(candlestick1,candlestick2,candlestick3): # bearish
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return (open1 < open2) and (close1 < close2) and (open1 < close1) and (open2 < close2) and ((open2 + close2) / 2 > close3) and (
		open3 > close3) and (open3 > close2) and (close3 > open2) and ((open3 - close3) / (.001 + (high3 - low3)) > .6)

def isBullishHarami(candlestick1,candlestick2,candlestick3): # bullish
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return (open1 > open2) and (close1 > close2) and (open1 > close1) and (open2 > close2) and (close3 > open3) and (close3 < open2) and (
		close2 <= open3) and ((close3 - open3) < (open2 - close2) * .3)

def isBearishHarami(candlestick1,candlestick2,candlestick3): # bearish
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();

	return (open1 < open2) and (close1 < close2) and (open1 < close1) and (open2 < close2) and (close3 < open3) and (close3 > open2) and (
		close2 > open3) and ((open3 - close3) < (close2 - open2) * .3)

def isMorningStar(candlestick1,candlestick2,candlestick3,candlestick4): #bullish
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();
	open4, close4, low4, high4 = candlestick4.getProperties();

	return (open1 > open2) and (close1 > close2) and (open1 > close1) and (open2 > close2) and (open3 < close2) and isDoji(candlestick3) and (
		open4 > close3) and (close4 > open4) and (close3 < close2)

def isEveningStar(candlestick1,candlestick2,candlestick3,candlestick4): #bearish
	open1, close1, low1, high1 = candlestick1.getProperties();
	open2, close2, low2, high2 = candlestick2.getProperties();
	open3, close3, low3, high3 = candlestick3.getProperties();
	open4, close4, low4, high4 = candlestick4.getProperties();

	return (open1 < open2) and (close1 < close2) and (open1 < close1) and (open2 < close2) and (open3 < close2) and isDoji(candlestick3) and (
		open4 < close3) and (close4 < open4) and (close3 > close2)

def identifyAll(candlestick1, **candlesticks):
	candlestick2 = candlesticks.get("candlestick2")
	candlestick3 = candlesticks.get("candlestick3")
	candlestick4 = candlesticks.get("candlestick4")

	if (candlestick4):
		if (isMorningStar(candlestick1,candlestick2,candlestick3,candlestick4)): print ("--Morning Star")
		if (isEveningStar(candlestick1,candlestick2,candlestick3,candlestick4)): print ("--Evening Star")
	elif (candlestick3):	
		if isBullishBeltHold(candlestick1, candlestick2, candlestick3): print ("--Bullish Belt Hold")
		if isBearishBeltHold(candlestick1, candlestick2, candlestick3): print ("--Bearish Belt Hold")
		if isHammer(candlestick1, candlestick2, candlestick3): print ("--Hammer")
		if isInvertedHammer(candlestick1, candlestick2, candlestick3): print ("--Inverted Hammer")
		if isPiercingLine(candlestick1,candlestick2,candlestick3): print ("--Piercing Line")
		if isDarkCloud(candlestick1,candlestick2,candlestick3): print ("--Dark Cloud")
		if isBullishHarami(candlestick1,candlestick2,candlestick3): print ("--Bullish Harami")
		if isBearishHarami(candlestick1,candlestick2,candlestick3): print ("--Bearish Harami")
	elif(candlestick2):
		if isBullishEngulfing(candlestick1, candlestick2): print ("--Bullish Engulfing")
		if isBearishEngulfing(candlestick1, candlestick2): print ("--Bearish Engulfing")
	elif (candlestick1):
		if isDoji(candlestick1): print ("--Doji")
		if isGreenMarubozu(candlestick1): print ("--Green Marubozu")
		if isRedMarubozu(candlestick1): print ("--Red Marubozu")
		if isDragonflyDoji(candlestick1): print ("--Dragonfly Doji")
		if isGravestoneDoji(candlestick1): print ("--Gravestone Doji")



# print (isHammer(Candlestick(40,30,28,44), Candlestick(39,25,24,44), Candlestick(25,25,10,28)))