import  numpy as np
#97-122 : a-z
def letters_point():
    #make letter list
    letter=[chr(n) for n in range(97,123)]
    #make list for 1
    one=np.ones(26,dtype=int)
    #combine two data
    Sets=dict(zip(letter,one))
    #Update special score
    #change=[]
    # change.append({'d':2,'g':2})
    # change.append({'b':3,'c':3,'m':3})
    # change.append({'f':4,'h':4,'v':4,'w':4,'y':4})
    # change.append({'k':5})
    # change.append({'j':8,'x':9})
    # change.append({'q':10,'z':10})
    # for i in range(len(change)):
    #     Sets.update(change[i])
    # The same above code
    change={'dg':2,'bcm':3,'fhvwy':4,'k':5,'jx':8,'qz':10}
    for key in Sets.keys():
        for k in change.keys():
            if key in k:
                Sets[key]=change[k]
                break
    return Sets
#--------------------------------------------------------------
def maxScore_word(data):
    #make dictionary obtains words and their scores
    scores={}
    for wd in data:
        points=0
        if len(wd.strip())>0:
            for c in wd.strip():
                points+=scores_set[c.lower()]
            scores[wd]=points
    return max(scores,key=lambda x:scores[x])
#--------------------------------------------------------------
#Main code
try:
    words=input('Words: ').strip().split(',')
    assert len(words)<=10
    scores_set=letters_point()
    print(maxScore_word(words))
except :
    print('Invalid input words')