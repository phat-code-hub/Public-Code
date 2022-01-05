#Reverse array result
def reverse_array(data):
    rev_data=[]
    for datum in data:
        rev_datum=datum[::-1]
        rev_data.append(rev_datum)
    return rev_data[::-1]
#-------------------------------------  
def show(data):
    for datum in data:
        array=' '.join(datum)
        print(array)
#-------------------------------------
line=int(input('How many line :')) 
rows=[]
num=1
for i in range(1,line+1):
    array=[]
    for j in range(1,i+1):
        array.append(str(num))
        num+=1
    rows.append(array)
rev_rows=reverse_array(rows)
print('Floyd\'s triangle:')
show(rows)
print()
print('Reverse Floyd\'s triangle:')
show(rev_rows)