import requests
import json
from FinClasses import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}

def cleanHTML(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def getName(text):
    if text.find("title=") != -1:
        text = text[ (text.find("title=")+7) : -1]
        text = text[0: text.find('"')]
        return(text)
    else:
        return text
        
def getTicker(text):
    if text.find(" ") != -1:
        return text[0: text.find(" ")]
    else:
        return text

def getWeight(text):
    if text == "NA":
        return 0.0
    else:
        return float(text)

def getTotalWeight(ETFTicker, stockList):
    weight = 0.0
    for stock in stockList:
        weight += stock.getWeight()
    print("Percent of fund obtained:", ETFTicker, str(round(weight, 2)) + "%")
    print("----------------------------------------------------")

def getETFInfo(ETFTicker):
    url = "https://www.zacks.com/funds/etf/{}/holding"
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url.format(ETFTicker))
        print(f"Extracting: {r.url}")
        stockList = []
        for line in r.text.splitlines():
            if not line.startswith('etf_holdings.formatted_data'):
                continue
            data = json.loads(line[30:-1])
            for holding in data:
                name = getName(holding[0])

                stockTicker = cleanHTML(holding[1])
                stockTicker = getTicker(stockTicker)

                weight = getWeight(cleanHTML(holding[3]))
                newStock = stock(name, stockTicker, weight)
                stockList.append(newStock)
            break
        getTotalWeight(ETFTicker, stockList)
        return stockList

