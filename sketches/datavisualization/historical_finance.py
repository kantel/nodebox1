import matplotlib.finance as mpf

size(480, 480)
background(0, 0.1172, 0.2344)
# color(HSB)

names = ["EMES", "TSLA", "FLT", "FRF", "SAN", "MTNOY", "XLF", "VIG", "C", "EUM"]
date1 = (2010, 1, 1)
date2 = (2014, 7, 2)
Q = {}
C = {}

for i in names:
    # print(i)
    # print(names[1])
    
    quotes = mpf.quotes_historical_yahoo_ohlc(i, date1, date2)
    

