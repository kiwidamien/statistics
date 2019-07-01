import numpy as np
import pandas as pd

np.random.seed(42)

N_values = [200 + 25*week_num for week_num in range(60)]
defects  = [np.random.binomial(n, p=0.08) for n in N_values]

pd.DataFrame({'defects': defects, 'tires ordered': N_values}).to_csv('defects.csv',
                                                                     index=False)
