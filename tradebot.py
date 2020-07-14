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

def authenticate():
    """ Method checks credentials and logs user in. """
    pass

def predictions():
	""" TODO set up cronjob to make market predictions."""
	# 2-3 day price windows are insufficient
	# 10 and 50 windows work much better
	pass

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
