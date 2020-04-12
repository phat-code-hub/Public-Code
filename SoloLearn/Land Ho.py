WAITTING_TIME=10
LIMIT_PEOPLE=20
people_ahead=int(input('waitting people: '))
if (people_ahead+1) % LIMIT_PEOPLE ==0:
    board_waitting=people_ahead // LIMIT_PEOPLE
else:
    board_waitting=(people_ahead+1) // LIMIT_PEOPLE
time_to_Beach=board_waitting*WAITTING_TIME*2+WAITTING_TIME
print(time_to_Beach)