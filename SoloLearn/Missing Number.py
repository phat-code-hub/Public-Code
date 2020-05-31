import  numpy as np
import pandas as pd
lst=[float(x) if x!='nan' else np.nan for x in input().split()]
df0=pd.DataFrame(lst)
df0.fillna(df0.mean(),inplace=True)
df=df0.copy().applymap(lambda n:round(n,1))
tp='dtype: '+str(df0[0].dtypes)
print(df.to_string(header=False,col_space=4,float_format='{:.1f}'.format))
print(tp)