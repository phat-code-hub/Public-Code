def binary_search(value,data):
    chk=-1
    times=0
    if float(value) >= float(data[0]) and float(value) <= float(data[-1]):
        try:
            left_bound=0
            right_bound=len(data)-1
            while left_bound<=right_bound:
                mid=(left_bound+right_bound)//2
                if mid>0:
                    times +=1
                    if data[mid] ==value:
                        chk=mid
                        break
                    elif float(data[mid]) < float(value):
                        left_bound=mid
                    else:
                        right_bound=mid
                else:
                    break
        except:
            chk=-2
    return chk,times
data_str=input('Data : ').strip()
search_Value=input('Search Value:').strip()
sep=',' if ',' in data_str else ' '
data0=data_str.split(sep)
try:
    datas=[float(n) for n in data0]
    # datas=sorted(data1)
    datas=sorted(datas)
    code,repeat_Times=binary_search(search_Value,datas)
    if code == -2:
        print('Invalid Value')
    elif code == -1:
        print('Not Found')
    else:
        print('Found at position: {0} atfer {1} searched times'.format(code,repeat_Times))
except:
    print('Invald Number')