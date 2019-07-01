import pandas as pd
import numpy as np

np.random.seed(42)
Lambda = 18.0

num_calls = np.random.poisson(Lambda, size=22*5)

pd.DataFrame({'num_calls': num_calls}).to_csv('calls.csv', index=False)
