TICKET=12 # 1 ticket= 12 Points
try:
    points_scored=int(input('Points: '))
    gun_cost_by_ticket=int(input('cost: '))
    ticket_exchange=points_scored//TICKET
    if ticket_exchange>=gun_cost_by_ticket:
        print('Buy it!')
    else:
        print('Try again')
except:
    print('Invalid Number')