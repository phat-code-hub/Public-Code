def linear_search(check_value,data):
    chk=-1
    times=0
    try:
        value=float(check_value)
        for pos in range(len(data)):
            times +=1
            if float(data[pos]) == value:
                chk=pos+1
                break
    except:
        chk=-2
    return chk,times
data_str=input('Data: ').strip()
search_Value=input('Search Value:').strip()
sep=',' if ',' in data_str else ' '
datas=data_str.split(sep)
code,repeat_Times=linear_search(search_Value,datas)
if code == -2:
    print('Invalid Value')
elif code == -1:
    print('Not Found')
else:
    print('Found at position: {0} atfer {1} searched times'.format(code,repeat_Times))