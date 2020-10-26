import sys
from scipy.interpolate import UnivariateSpline
import numpy as np

n = int(sys.stdin.readline())

raw_prices = []

for i in range(0, n):
    line = sys.stdin.readline()
    timestamp, price = line.split("\t")
    raw_prices.append(price)

prices_ind = []
missing_prices_ind = []
prices = []

for i in range(0, n):
    if 'Missing' in raw_prices[i]:
        missing_prices_ind.append(i)
    else:
        prices_ind.append(i)
        prices.append(float(raw_prices[i]))

#Splie Interpolation
spline = UnivariateSpline(np.array(prices_ind), np.array(prices), s=2)
for i in missing_prices_ind:
    print(spline(i))
