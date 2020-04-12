WAITTING_TIME=10
LIMIT_PEOPLE=20
people_ahead=int(input('waitting people: '))
if (people_ahead+1) % LIMIT_PEOPLE ==0:
    board_ship_order=(people_ahead+1) // LIMIT_PEOPLE
else:
    board_ship_order=(people_ahead+1) // LIMIT_PEOPLE +1
time_to_board=board_ship_order*WAITTING_TIME
print(time_to_board)