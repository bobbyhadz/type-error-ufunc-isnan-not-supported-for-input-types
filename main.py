# TypeError: ufunc 'isnan' not supported for the input types

import numpy as np
import pandas as pd

arr1 = np.array(['5', '10', '15'])

# [False False False]
print(pd.isnull(arr1))

arr2 = np.array(['5', '10', '15', None, np.nan])

# [False False False  True  True]
print(pd.isnull(arr2))