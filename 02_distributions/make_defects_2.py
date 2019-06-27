import numpy as np
import pandas as pd

N = np.random.poisson(100, size=60)
defects = [np.random.binomial(n, p=0.08) for n in N]

pd.DataFrame({'defects': defects, 'order_size': N}).to_csv('defects_vary.csv',
                                                           index=False)
