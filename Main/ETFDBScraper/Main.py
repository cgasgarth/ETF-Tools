from ETFDBScraper import *
import sys

sys.path.insert(0, "../SharedTools")
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