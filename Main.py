from ETFInfo import *
from FinClasses import *
from FinClasses import *

keys = ["SMH"]

def main(keys):
    ETFlist = []
    for key in keys:
        newETF = ETF(key)
        holdings = getETFInfo(newETF.getTicker())
        newETF.setHoldings(holdings)
        ETFlist.append(newETF)
    for etf in ETFlist:
        print("INFO FOR:", etf.getTicker())
        for holding in etf.getHoldings():
            print(holding.getTicker(), holding.getWeight())



main(keys)