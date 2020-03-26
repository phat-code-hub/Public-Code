from collections import Counter
cards=('2','3','4','5','6','7','8','9','10','J','Q','K','A')
suits=('H','D','C','S') 
result_code={1:'High Card',2:'One Pair',3:'Two Pairs', \
            4:'Three of a Kind',5:'Straight',6:'Flush',7:'Full House', \
            8:'Four of a Kind',9:'Straight Flush',10:'Royal Flush'}
#Sort by card set
def card_sorted(data):
    return list(sorted(data,key=lambda x: cards.index(x)))
#Check  Consecutiveness of cards 
def Consecutive_Check(data):
    data1=data[:-1]
    data2=data[1:]
    data3=[]
    for i in range(0,len(data1)):
        data3.append(cards.index(data2[i])-cards.index(data1[i]))
    return all(n == 1 for n in data3)
#Input data and calculate
Pokers=input('Five cards :').strip().split()
card=[]
suit=[]
code=0
for c in Pokers:
    card.append(c[:-1].upper())
    suit.append(c[-1].upper()) 
card= card_sorted(card)
countList=dict(Counter(card))
repeat_list=sorted(countList.values(),reverse=True)
repeat_list_len=len(repeat_list)
if repeat_list_len == 2: # [4,1] Four of a Kind , [3,2] : Full House
    if repeat_list[0]==4:
        code=8
    else :
        code =7
if repeat_list_len == 3:   #[3,1,1] : Three of a Kind ,[2,2,1]: Two Pair
    if repeat_list[0]==3:
        code=4
    else :
        code =3
if repeat_list_len == 4: #[2,1,1,1] One Pair
    code =2
if repeat_list_len == 5:
    isSameSuit=suit.count(suit[0]) == 5
    isConsecutive=Consecutive_Check(card)
    if isSameSuit: 
        if isConsecutive: 
            if card[-1] == 'A': #Royal Flush
                code =10
            else:
                code =9 # Straight Flush
        else: # Flush
            code =6
    else:
        if isConsecutive: 
            code =5 # Straight
        else: # High Card
            code =1
print(result_code[code])