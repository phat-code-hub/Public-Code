import random
MAX=30
pl_pos=1
com_pos=1
def banmen():
    print('.'*pl_pos+'P'+'.'*(MAX-pl_pos))
    print('.'*com_pos+'C'+'.'*(MAX-com_pos))
while True:
    banmen()
    input('Enter to move your position')
    pl_pos +=random.randint(1,6)
    if pl_pos>MAX:
        pl_pos=MAX
    # banmen()
    if pl_pos==MAX:
        print('YOU WIN!')
        break
    com_pos +=random.randint(1,6)
    if com_pos>MAX:
        com_pos=MAX
    # banmen()
    if com_pos==MAX:
        print('COMPUTER WIN!')
        break