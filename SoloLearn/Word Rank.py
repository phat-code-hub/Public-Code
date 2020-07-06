from collections import Counter
word_list=[]
repeat_list=[]
orders=[]

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

def AnalyseWord(word):
    letters_info=Counter(word)
    sum_cases=fact(len(word))
    for k,v in letters_info.items():
        if v>1 :
            sum_cases //=fact(v)
    wds=list(letters_info.keys())
    wds=sorted(wds)
    repeat_times=[fact(i-1) for i in range(len(wds),1,-1)]
    repeat_times.append(0)
    return wds,repeat_times
#--------------------------------------------
def findOrder(data):
    lst=[]
    pos=[]
    global word_list,repeat_list
    for s in data:
        id=word_list.index(s)
        lst.append(id)
    print(lst)
    ord=0
    for n in range(len(lst)):
        if n==0:
            ord=lst[n]*repeat_list[n]+1
        else:
            if lst[n]>0:
                ord  = ord+ (lst[n]-n+1)*repeat_list[n]
        pos.append(ord)
    return pos
#--------------------------------------------
#Main Code
str_= input('String: ').strip().upper()
word_list,repeat_list=AnalyseWord(str_)
print(word_list,repeat_list)
orders=findOrder(str_)
print(orders)
print(orders[-1])