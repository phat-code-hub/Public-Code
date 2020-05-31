import  numpy as np
import pandas as pd
lst=[float(x) if x!='nan' else np.nan for x in input().split()]
df=pd.DataFrame(lst)
df.fillna(df.mean(),inplace=True)
tp='dtype:'+str(df[0].dtypes)
print(df.to_string(header=False,float_format='{:.1f}'.format))
print(tp)