DISCOUNT=0.1 # 10%
TAX=1.07 # 7%
PRICE=5.00
num =gets()
sum= num.to_i*PRICE
if num.to_i >1
    sum *=(1-DISCOUNT)
end
sum *= TAX
puts sum