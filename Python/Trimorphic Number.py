def isTrimorphic(number):
    try:
        length=len(str(number))
        triple_num=number**3
        triple_num_str=str(triple_num)
        check_part=triple_num_str[len(triple_num_str)-length:]
        return int(check_part) == number
    except :
        print('It is not a number')
#-----------------------------------------------------------------------------------
def checkRange(down,up):
    if down>up:
        down,up=up,down
    Trimorphic_list=[]
    for i in range(down,up+1):
        if isTrimorphic(i):
            Trimorphic_list.append(str(i))
    #you can use this simple code instead above for loop
    #Trimorphic_list=[str(n)  for n in range(down,up+1) if isTrimorphic(n)==True]
    return Trimorphic_list
#-----------------------------------------------------------------------------------
phrase=input('input one number or two limit (a,b) for checking Trimorphicrphic: ').strip()
if len(phrase)>0:
    nums=phrase.split(',')
    if len(nums) ==1: # check one  number
        print('true ' if isTrimorphic(int(nums[0])) else 'false')
    else: # check all number in range
        try:
            downlimit=int(nums[0])
            uplimit=int(nums[1])
            result=checkRange(downlimit,uplimit)
            print('There are {0} trimorphic numbers from range {1} to {2}:'.format(len(result),downlimit,uplimit))
            print(','.join(result))
        except :
            print('Invalid limits')
else: 
    print('Nothing!')