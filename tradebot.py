#!/usr/bin/env python3
"""
Bot used to initiate trades with robinhood account.
"""

__author__ = "Cody Flickenschild"
__version__ = "0.1.0"
__license__ = "MIT"

# python interface used to interact with robinhood api
# https://github.com/jmfernandes/robin_stocks

def authenticate():
    """ Method checks credentials and logs user in. """
    pass

def predictions():
	""" TODO set up cronjob to make market predictions."""
	# 2-3 day price windows are insufficient
	# 10 and 50 windows work much better
	pass

def main():
    """ Main entry point of the app """
    # TODO add as much logging as I can.
    # people who have done this regret not adding more.
    print("Let's trade.")


if __name__ == "__main__":
    """ This is executedS when run from the command line """
    main()
