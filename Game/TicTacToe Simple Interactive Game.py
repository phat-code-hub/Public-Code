"""
    How to Play Tic-Tac-Toe
    1-Set Up the Game:

        Draw a grid with 3 rows and 3 columns. You'll have 9 squares in total.

    2-Players:

        There are two players. One player is "X" and the other player is "O".

        Taking Turns:

        Players take turns to place their mark (X or O) in an empty square on the grid.

        Player "X" usually goes first.

    3-Winning the Game:

        The goal is to get three of your marks in a row. This can be horizontally, vertically, or diagonally.

        The first player to get three in a row wins!

    4-Ending the Game:

        If all nine squares are filled and no player has three in a row, the game is a tie.
"""
import math
def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print("--+---+--")
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print("--+---+--")
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_win(board,player):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] ==board[b]==board[c]== player 
            for a,b,c in win_conditions)

def check_draw(board):
    return all(spot != " " for spot in board)

def minimax(board,depth,is_maxminizing):
    if check_win(board,'0'):
        return 1
    if check_win(board,'X'):
        return -1
    if check_draw(board):
        return 0
    
    if is_maxminizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] ="0"
                score = minimax(board,depth+1,False)
                board[i] = " "
                best_score = max (score,best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] ="X"
                score = minimax(board,depth+1,True)
                board[i] = " "
                best_score = min (score,best_score)
        return best_score
        
        
def cpu_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] ="O"
            score = minimax(board,0,False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def tic_tac_toe():
    board = [" "]*9
    current_player = "X"
    
    
    # print("三目並べゲーム開始！")
    # print("プレイヤーが'X' で,CPUが'O'です。")
    
    print("Tic Tac Toe GAME start!")
    print("Player :X ,CPU :O")
    
    while True:
        display_board(board)
        if current_player == "X":
            try:
                # move = int(input("プレイヤーの番です。1-9の位置を選んで下さい。"))-1
                move = int(input("Player turn. Choose a cell number (1-9) please: "))-1
                if  board[move] != " ":
                    print("This place was filled!, select other cell please!")
                    # print("その場所はすでに埋まっています。別の場所を選んで下さい。")
                    continue
            except(ValueError,IndexError):
                print("Invalid input.Please choose right cell number from 1-9:")
                # print("無効な入力です。１から９までの数値を入力したください。")
                continue
        else:
            # print("CPUの番です。")
            print("CPU turn!")
            move = cpu_move(board)
        
        board[move] = current_player
        
        if check_win(board,current_player):
            display_board(board)
            # print(f"{current_player}の勝利です。" if current_player =="X" else "CPUの勝利です。" )
            print(f"Congratulation {current_player} won!" if current_player =="X" else " CPU Won!" )
            break
        
        if check_draw(board):
            display_board(board)
            # print("引き分けです。")
            print("Draw!")
            break 
            
        current_player = "O" if current_player =="X" else "X"

if __name__ == "__main__":
    tic_tac_toe()