import re
def check_String(word):
    reg_null=re.compile(r'(.)+') # not null
    reg_digit=re.compile(r'(\d)+') # no numeric letter
    m1=reg_null.search(word)
    m2=reg_digit.search(word)
    if m1 != None and m2 ==None:
        return True
    else:
        return False  
try:
    word=input('Origin String: ').strip()
    assert check_String(word)
    if len(word) ==1:
        print(word)
    else:
        compressed_word=''
        chk=word[0]
        count=1
        index=1
        while index <len(word):
            if (word[index]==chk):
                count+=1
            else:
                compressed_word +=chk
                if count>1:
                    compressed_word+=str(count)
                    count=1
                chk=word[index]
            index+=1
        compressed_word +=chk
        if count>1:
            compressed_word +=str(count)
        print(compressed_word)
except :
    print('Incompatible String!')