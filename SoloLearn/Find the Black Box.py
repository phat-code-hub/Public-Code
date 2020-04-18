import numpy as np
#Ideas of this solution:
#1) Make a standard weight box list (>=10Kg and <=20kg)
#2)Replace 1 any box's weight by abnormal one
#3)Find this box and return index and it's abnormal weight
#-------------------------------------------------------------
#These constants can be updated in future if possible
TOTAL=100
MIN_WEIGHT=10
MAX_WEIGHT=20
def prepareData():
    boxes=np.random.randint(MIN_WEIGHT,MAX_WEIGHT,TOTAL)
    #make two abnormal weights in two outside standard weight
    abnormal_weight=[np.random.randint(1,MIN_WEIGHT-1),np.random.randint(MAX_WEIGHT+1,MAX_WEIGHT+100)]
    #choice one candidate from list
    candidate_choice=np.random.choice(abnormal_weight)
    random_index=np.random.randint(0,99)
    #change any box by abnormal weight
    boxes[random_index]=candidate_choice
    return boxes
#Main Code
box=prepareData()
print('Box list:')
print(box)
res=[k for k,v in enumerate(box) if v<10 or v>21]
print('The box {0} ({1}Kg) is outside the range.'.format(res[0]+1,box[res[0]]))