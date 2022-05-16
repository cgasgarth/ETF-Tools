import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}


def cleanHTML(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):
    req = requests.Session()
    return req.get(url)
 
def getJSONS(ticker):
    url = "https://etfdb.com/etf/{}/#charts"
    jsonList = []
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url.format(ticker))
        print(f"Extracting: {r.url}")
        for line in r.text.splitlines():
            if line.startswith("<table class='chart base-table' data-chart-series="):
                # print(line[line.find("[",):line.rfind("]") + 1])
                # print()
                # print("-------------------------------------------------------")
                # print()
                newJSON = json.loads(line[line.find("[",):line.rfind("]") + 1])
                #if the json is not empty append to the jsonList
                if newJSON != []:
                    jsonList.append(newJSON)
    return jsonList