# %%
import pandas as pd

data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index = index)
print(series)

#%%
import pandas as pd
df = pd.DataFrame(
    data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
    index = ['a','b','c','d'],
    columns= ['A', 'B', 'C', 'D']
)
print(df)
df.drop(['A', 'B'],axis=1)

# %%
