import sys
START=sys.argv[1] #スタート状態
FINAL ="12345678_"#解かれた状態
LEFT =-1
RIGHT=1
UP=-3
DOWN=3

queue=[]
checked=set()
route={}
path=[FINAL]
 #スタート状態を格納
queue.append(START)
def move(board,dir,pos):
    b=board.replace("_","R")
    c=board[pos+dir]
    b=b.replace(c,"_")
    b=b.replace("R",c)
    if  b not in checked:
        queue.append(b)
        checked.add(b)
        route[b]=board
def solve():
    board =queue.pop(0)
    if board == FINAL:
        return False
    pos = board.find("_")
    if pos == 0:
        move (board,RIGHT,0)
        move(board,DOWN,0)
    elif pos == 1:
        move (board,LEFT,1)
        move(board,RIGHT,1)
        move(board,DOWN,1)
    elif pos == 2:
        move (board,LEFT,2)
        move(board,DOWN,2)
    elif pos == 3:
        move(board,RIGHT,3)
        move (board,UP,3)
        move(board,DOWN,3)
    elif pos == 4:
        move (board,LEFT,4)
        move(board,RIGHT,4)
        move (board,UP,4)
        move(board,DOWN,4)
    elif pos == 5:
        move (board,LEFT,5)
        move (board,UP,5)
        move(board,DOWN,5)
    elif pos == 6:
        move(board,RIGHT,6)
        move (board,UP,6)
    elif pos == 7:
        move (board,LEFT,7)
        move(board,RIGHT,7)
        move (board,UP,7)
    elif pos == 8:
        move (board,LEFT,8)
        move (board,UP,8)
    return True
while solve():
    pass
#スタート状態から
#解かれた状態までの遷移を
#Pathに格納
b=route[FINAL]
while b!= START:
    path.insert(0,b)
    b=route[b]
path.insert(0,START)
#pathを表示
for p in path:
    print (p[:3])
    print(p[3:6])
    print(p[6:])
    print("")