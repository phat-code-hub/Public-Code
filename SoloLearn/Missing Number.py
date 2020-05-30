import  numpy as np
import pandas as pd
lst=[float(x) if x!='nan' else np.nan for x in input().split()]
mid=0.0
list=[]
list_=np.array(lst)
for n in list_:
    if n==np.nan:
        list.append(mid)
    else:
        list.append(round(n,1))
print(list)
# df=pd.DataFrame(list)
# df.replace(np.nan,df.mean(),inplace=True)

# print(df)