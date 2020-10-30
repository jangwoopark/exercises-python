import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.holtwinters import ExponentialSmoothing

n = int(input())

data = []
for _ in range(n):
    data.append(input())

visitors = np.array([int(row) for row in data])

model = ExponentialSmoothing(visitors, trend="add", damped=True, seasonal="add", seasonal_periods=7)
results = model.fit()

forecasts = results.forecast(30)
for predcited in forecasts:
    print(predcited)
