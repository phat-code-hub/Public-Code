# This code is used for beginner play at tea time 
#This shows the today's fortune by chance and 
# varies by each choice
# this code use if syntax
# --Create by Ueda--
import random
num = random.randint(0,6)
msg0="Today you are"
msg =""
if num == 0:
    msg ="very good luck!"
elif num == 1:
    msg = "average good luck"
elif num == 2:
    msg = "luck"
elif num == 3:
    msg ="normal"
elif num ==  4:
    msg ="bad!"
elif num == 5:
    msg ="rather bad"
else:
    msg= "very bad!!"
print (msg0,msg)