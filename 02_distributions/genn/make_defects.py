import numpy as np
import pandas as pd

N = 100

pd.DataFrame({'defects': np.random.binomial(N, p=0.08,
                                            size=60)}).to_csv('defects.csv',
                                                              index=False)
