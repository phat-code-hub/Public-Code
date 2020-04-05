def check_Prime(data):
    for i in range(1,int(len(data)//2)+1):
        #extract subword from first letter , loop until half of word length 
        key=words[0:i]
        #count exist times of key in word
        count=words.count(key)
        if len(key)*count == len(words):
            return 'not prime'
            break
    return 'prime'
words=input('string: ').strip()
print(check_Prime(words))