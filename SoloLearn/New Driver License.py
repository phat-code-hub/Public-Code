WAITINGTIME=20
myName=input('your name: ').strip()
agent=int(input('Available Agent: '))
people0=input('Waiting peole: ').strip()
peoples=people0.split()
peoples.append(myName)
peoples.sort()
my_Order=peoples.index(myName)
my_Waiting_Group=my_Order//agent
waiting_time=(my_Waiting_Group+1)*WAITINGTIME
print(waiting_time)