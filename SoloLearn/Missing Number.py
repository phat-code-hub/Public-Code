import  numpy as np
import pandas as pd
lst=[float(x) if x!='nan' else np.nan for x in input().split()]
df=pd.DataFrame(lst,dtype=float)
mid=df.mean()
df.fillna(mid,inplace=True)
df[0]=df[0].map('{:,.1f}'.format)
print(df[0].to_string())