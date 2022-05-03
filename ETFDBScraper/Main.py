from ETFDBScraper import *
import os, inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from ExcelTools import *
from FinClasses import *


def main(fileName):
    ETFs = importFromExcel(fileName)
    for ETF in ETFs:
        jsonList = getJSONS(ETF.getTicker())
        ETF.setJsonList(jsonList)
    firstETF = ETFs[0]
    firstETFJSON = firstETF.getCountryJSON()
    #print each json inside this json object
    for json in firstETFJSON:
        print(json)

main("../Current Portfolio.xlsx")