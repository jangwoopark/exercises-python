import numpy as np
import pandas as pd
for _ in range(int(input())): # loop test cases
    _ = input() # do not need N
    df = pd.DataFrame(np.array([input().split() for _ in range(6)], float).T)
    print(df.corr('kendall')[0][1:].argmax())
