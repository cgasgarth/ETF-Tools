from StockWebScraper import *
import os, inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from ExcelTools import *
from FinClasses import *
from FinTools import *


def main(fileName):
    ETFList = importFromExcel(fileName)
    for ETF in ETFList:
        if ETF.getTicker() == "HEWG":
            holdings = getETFInfo("EWG")
        else:
            holdings = getETFInfo(ETF.getTicker())
        ETF.setHoldings(holdings)
    print("----------------------------------------------------")
    print("Portfolio stock weights, printing stocks over 1%")
    stockWeights = totalWeights(ETFList)
    for stock in stockWeights:
        if stock.getWeight() > 1:
            print(stock.getName(), stock.getTicker(), str(round(stock.getWeight(), 2)) + "%")
    print(getNumHoldings(ETFList))

main("../Current Portfolio.xlsx")