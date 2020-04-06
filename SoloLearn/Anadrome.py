def Analyse(data):
    chuoi=[]
    Tu=data
    l=len(Tu)
    if l>=3:
        for i in range(l):
            first=Tu[0]
            left=Tu[1:]
            chuoi.append(first+left)
            Tu=left+first
            l=len(Tu)
    else:
        print('too small')
    return chuoi
#word=input('String: ').strip()
word='abcd'
res=Analyse(word)
print(res)