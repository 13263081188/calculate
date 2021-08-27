import numpy as np
print(type(np.random.rand(10)))
import pandas as pd

chart_data = pd.DataFrame(
        np.random.randn(20, 4),
        columns=['a', 'b', 'c', 'd'])
chart_data.loc[:,'d'] = np.random.randn(20,1)
print(chart_data.head())
