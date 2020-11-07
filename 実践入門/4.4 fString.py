note='note'
title='book'
print(f'python practice {note}')
print(f'title={title},note= {note}') #3.8 before
print(f'{title=},{note=}')
print(f'{title.upper()}')
print(f'{title.upper()=}')
print('python practice : %s %.2f' % ('book',1.0))

# Print List
aa=[1,2,3,4,5]
a=list(map(lambda x:str(x),aa))
print(':'.join(a))
for i in aa:
    print(i,sep='?')
for i in aa:
    print(i,end='?')
print(aa[0],aa[1],sep="!")