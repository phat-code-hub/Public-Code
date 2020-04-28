persons=[]
#Simulate N person case
def simulate(num,holder):
    global persons
    killed=[]
    count=1
    print('origin ',show(persons,holder))
    status0=persons[holder-1:]+persons[:holder-1]
    sta=status0.copy()
    while len(sta)>2:
        print('step {0} : now = {1}, kill = {2} , next = {3}'.format(count,sta[0],sta[1],sta[2]))
        sta.remove(sta[1]) 
        sta=sta[1:]+sta[:1]
        count+=1
    print('surviver',sta[0])

def show(arr,sword,die=[]):
    arr_str=list(map(str,arr))
    arr_str[sword-1]=str(sword)+'=>'
    if len(die)!=0:
        for d in die:
            arr_str[die-1]=' '
    return ' '.join(arr_str)
#Main code
try:
    total=int(input('How many people: '))
    first_holder=int(input('First sword holder: '))
    persons=[n for n in range(1,total+1)]
    # calculate(total,first_holder)
    simulate(total,first_holder)
except :
    print('Invalid Number!')