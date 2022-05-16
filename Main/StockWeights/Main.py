import sys

from FinTools import *
from StockWebScraper import *

sys.path.insert(0, "../SharedTools")
from ExcelTools import *
from FinClasses import *


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
