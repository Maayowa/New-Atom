import numpy as np
import pandas as pd

num = np.array([1,2,3,4,5,5,6])
df = pd.DataFrame(num)
df
df2 = df.copy()
df2
df3 = pd.concat([df,df2], axis = 1)
df3

df5 = df- df2
