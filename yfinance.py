import yahoo_fin.stock_info as si

aapl_earnings_hist = si.get_earnings_history("0700.HK")
for earning in aapl_earnings_hist:
    print(earning)
    print("------------------------")