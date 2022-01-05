import  numpy as np
import pandas as pd
lst=[float(x) if x!='nan' else np.NaN for x in input().split()]
df=pd.DataFrame(lst)
df.fillna(df[0].mean(),inplace=True)
df.round(1)
tp='dtype: '+str(df[0].dtypes)
print(df.to_string(header=False,col_space=4,float_format='{:.1f}'.format,justify='justify'))
print(tp)