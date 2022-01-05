#This solution based on the reasons below:
#1)If the length of palindrome is even:
#     all letters of word must have even frequency of apperance 
#     (called : repeat times) for example in 'SolooloS' : S :2 , o :4,l:2
#2)If the length of palindrome is odd:
#    one (and only one) letter has odd repeat time ('madam','mamam')
#3)All rearranging word in same anadrome has unique length and also has
#   same letter characteristic (kind , repeate time)
# => we don mind what the given phase is but only need to know the  
#  frequency of the letters appear in the word to decide this phrase
# would be a anadrome or not

from collections import Counter
def Analyse(phrase):
    ans='no'
    length=len(phrase)
    num=list(Counter(phrase).values())
    IsEven=[n % 2 ==0 for n in num]
    Chk_All_Even=all(cond==True for cond in IsEven)
    odd_count=IsEven.count(False)
    if length % 2 ==0:
        if Chk_All_Even:
            ans= 'yes'
    else:
        if odd_count ==1:
            ans='yes'
    return ans
#----------------------------------------------
words=input('phrase: ').strip().split()
if len(words) ==1:
    print(Analyse(words[0]))
else:
    answer=[]
    for word in words:
        answer.append(Analyse(word))
    if all(a == 'yes' for a in answer):
        print('yes')
    else:
        print('no')