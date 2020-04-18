#Calculate the last number to show
def findMax(n):
    if n==1:
        return 1
    else:
        return findMax(n-1)+n
#-----------------------------------------------
def show_Triangle(lines,maxnum,isReversed=False):
    if not isReversed:
        showed_num=1
        print('Floyd Triangle:')
        for line in range(lines):
            inline_nums=''
            for count in range(1+line):
                inline_nums+=str(showed_num) +' '
                showed_num +=1 
            print(inline_nums.strip())
    else:
        print('Reversed Floyd Triangle:')
        showed_num=maxnum
        for line in range(lines):
            inline_nums=''
            for count in range(lines-line):
                inline_nums+=str(showed_num) +' '
                showed_num -=1 
            print(inline_nums.strip())
    print()
#-----------------------------------------------
#Main code
try:
    rows=int(input('How many line to show: '))
    assert rows>0
    showed_last_number=findMax(rows)
    show_Triangle(rows,showed_last_number)
    show_Triangle(rows,showed_last_number,True)
except :
    print('Row number must be positive number ')
