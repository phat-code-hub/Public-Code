import string
sentence=input('Words: ').strip()
symbol=''
if len(sentence)>0:
    for word in sentence:
        if word in string.ascii_letters or \
            word in string.digits or \
            word in string.whitespace:
            symbol +=word
    print(symbol)
else:
    print('Nothing')