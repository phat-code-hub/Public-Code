symbol='*'
persons=[]
#Simulate N person case
def simulate(num,holder):
    global persons
    killed=[]
    count=1
    print()
    print('step 0:',show(persons,holder))
    status0=persons.copy()
    sta=status0[holder-1:]+status0[:holder-1]
    while len(sta)>2:
        print('Step {0}: kill = {1} , next holder = {2}'.format(count,sta[1],sta[2]))
        killed.append(sta[1])
        print('=> ',show(status0,sta[2],killed))
        sta.remove(sta[1]) 
        sta=sta[1:]+sta[:1]
        count+=1
    print('The last killed person: ',sta[1])
    print('The surviver and also winner :',sta[0])

def show(arr,sword,die=[]):
    arr_str=list(map(str,arr))
    arr_str[sword-1]=str(sword)+symbol
    if len(die)!=0:
        for d in die:
            arr_str[arr_str.index(str(d))]=' '
    return '['+' '.join(arr_str)+']'
#Main code
try:
    total=int(input('How many people: '))
    first_holder=int(input('First sword holder: '))
    persons=[n for n in range(1,total+1)]
    # calculate(total,first_holder)
    simulate(total,first_holder)
except :
    print('Invalid Number!')