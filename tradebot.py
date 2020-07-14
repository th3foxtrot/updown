#!/usr/bin/env python3
"""
Bot used to initiate trades with robinhood account.
"""

__author__ = "Cody Flickenschild"
__version__ = "0.1.0"
__license__ = "MIT"

# python interface used to interact with robinhood api
# https://github.com/jmfernandes/robin_stocks
import yfinance
import time
from datetime import date

test_tickers = ['amd', 'tsla', 'tlt']
today = date.today()

class Portfolio:
	""" Class for portfolio object. """
	def __init__(self, balance):
		self.b = balance


def authenticate():
    """ Method checks credentials and logs user in. """
    pass

def predictions():
	""" TODO set up cronjob to make market predictions."""
	# 2-3 day price windows are insufficient
	# 10 and 50 windows work much better
	pass

def setPortfolio():
	""" Creates a brand new portfolio to be used by the bot. """
	balance = 1000
	pass

def updatePortfolio(action, quantity, cost):
	""" Updates portfolio with current prices. """
	# should be in Portfolio class?
	# calcuate value of every stock owned.
	# #ofstocks * price
	if action == 'b':
		print("Bought ", quantity, "of ", ticker, "at ", cost)
	elif action == 's':
		print("Sold ", quantity, "of ", ticker, "at ", cost)
	# TODO cleanup print statement for accurate testing.
	# TODO logging of every transaction
	pass

def buyStock():
	""" Buys stock and adds it to portfolio. """
	# getPrice()
	# getPrice() * quantity purchased
	# updatePortfolio()

def sellStock():
	""" Sells stock and removes it from portfolio. """
	# getPrice()
	# get

def dailyHigh(ticks):
	tick_count = 0
	for i in ticks:
		print(test_tickers[tick_count], i.history("1d").at[today, 'High'])
		# print(i.history("1d").at[today, 'High'])
		tick_count = tick_count + 1
		# Daily High is misleading....
		# Test today. tsla's high was 1700 closed closer to 1400

def main():
    """ Main entry point of the app """
    # TODO add as much logging as I can.
    # people who have done this regret not adding more.
    print("Let's trade.")
    formatted_ticks = []
    for i in test_tickers:
    	formatted_ticks.append(yfinance.Ticker(i.upper()))
    dailyHigh(formatted_ticks)


if __name__ == "__main__":
    """ This is executedS when run from the command line """
    main()
