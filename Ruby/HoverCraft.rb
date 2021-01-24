 PRICE = 3000000
 INSURANCE = 1000000
 MONTHLY_CAPACITY = 10
 UNIT_COST = 2000000
 customer= gets().to_i
 expence = MONTHLY_CAPACITY * UNIT_COST + INSURANCE
 income = customer*PRICE
 if income > expence 
    puts "Profit"
 elsif income == expence 
    puts "Broken Even"
 else 
    puts "Loss"
 end