#!/usr/bin/env python3
"""
Pull and Display Data For Tickers
"""

__author__ = "Cody Flickenschild"
__version__ = "0.1.0"
__license__ = "MIT"

import yfinance
import time

amd = yfinance.Ticker("AMD")

def intro():
    """Runs on startup."""
    print("\n\"Rule No.1: Never lose money")
    print("Rule No.2: Never forget rule No.1\"")
    print("-Warren Buffett")
    print("\nAll info is provided by Yahoo Finance\nI am not a professional financial advisor.\n\n")

def repeat():
    input("\nPress enter when you would like to continue.\n")

def ticker_choice():
    tckrChoice = input("What stock are you looking for information about? ")
    print(tckrChoice.upper())
    return yfinance.Ticker(tckrChoice.upper())

def command(ticker):
    print("\nCommands: \n'info'\n'history'\n'recommendations'\n'options'\n'quit'")
    return input("Enter a command: ")

def ticker_info(ticker):
    """Grab price of stock."""
    # TODO implement error checking for api call
    # is info good?
    return ticker.info

def options(ticker):
    """Display commands to interact with options trading."""
    # TODO specific expiration command
    optChoice = input("Would you like to see 'all' option or a specific 'expiration'? ")
    if optChoice == 'all':
        print(ticker.options)
    elif optChoice == 'expiration':
        expire = input("What is the specific date? 'YYYY-MM-DD' ")
        updown = input("'calls' or 'puts'? ")
        if updown == 'calls':
            tckrcall = ticker.option_chain(expire).calls
            print(ticker.option_chain(expire).calls)
            #--------------------------------
            # This is a pandas.DataFrame
            # TODO research how to manipulate.
            print(type(tckrcall))
            #--------------------------------
        elif updown == 'puts':
            print(ticker.option_chain(expire).puts)
        else:
            print("Please select 'calls' or 'puts' ")

def yhistory(ticker):
    """Asks user specific commands relating to stock historical data."""
    hisChoice = input("Would you like 'recent' history or 'specific'? ")
    if hisChoice == 'recent':
        print(ticker.history())
    elif hisChoice == 'specific':
        date = input("What is the date that you are looking for data on? ")
        print(ticker.history(date))

def main():
    """ Main entry point of the app """
    # TODO main loop must be in a while loop
    # TODO receive input from the user for a ticker
    # print(current_price(amd))
    ticker = None
    intro()
    while True:
        if ticker == None:
            ticker = ticker_choice()
        else:
            choice = command(ticker)
            if choice == 'info':
                # TODO format json
                print(ticker_info(ticker))
                repeat()
                # we're getting fuzzy here. we're stuck
                intro()
                # what was going on here?? ^ TODO
            elif choice == 'financials':
                # RETURNS empty data frame IN ALL TESTED INSTANCES
                finChoice = input("'financials' or 'quarterly_financials'?")
                if finChoice == 'financials':
                    print(ticker.financials)
                elif finChoice == 'quarterly_financials':
                    print(ticker.quarterly_financials)
                else:
                    print("\nPlease choose one of the options above!\n")
                    time.sleep(2)
            elif choice == 'recommendations':
                print(ticker.recommendations)
            elif choice == 'sustainability':
                # RETURNS NONE IN ALL TESTED INSTANCES
                if ticker.sustainability == None:
                    print("\nSorry, nothing to display here.\n")
                else:
                    print(ticker.sustainability)
            elif choice == 'options':
                options(ticker)
            if choice == 'history':
                # TODO ask user for specific time?
                # refer to link below for yfinance use.
                yhistory(ticker)
                # print(ticker.history())
                # https://aroussi.com/post/python-yahoo-finance
            if choice == 'testcase':
                print(type(ticker.history("3d")))
                print(ticker.history("3d").at['2020-07-09', 'Close'])
            elif choice == 'quit':
                print("Goodbye.")
                break
            else:
                print("\nPlease choose one of the commands listed above.\n")
                # Sleeps before printing when I uncomment the below line...
                # time.sleep(2)

#############################################
# Get value at specified row/column pair.
# ticker.history("3d").at[2020-07-09, Close]
# result should be 57.26
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at
#############################################


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
