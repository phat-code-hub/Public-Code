#Return the exchange results based on calculating by descending order of coin values
def greedy(coin_list,n):
    change_list ={}
    coin_list.sort(reverse =True)
    #Initial change list
    for c in coin_list:
        change_list[c] =0
    
    for coin in coin_list:
        if n >= coin:
            change_list[coin] += n // coin
        n %= coin
    # print(change_list)
    print("The exchange detail: ")
    for k,v in change_list.items():
        if v>0:
            print("{0:4d} : {1:3d} pieces ".format(k,v))
#--------------------------------------
# main code
if __name__ == '__main__':
    available_coin_list=[10,50,100,500] # list of available coins optionally
    amount_str=input("Exchange amount: ") 
    try:
        payment_amount =int(amount_str)
    except:
        print("invalid number format!")
    else:
        greedy(available_coin_list,payment_amount)