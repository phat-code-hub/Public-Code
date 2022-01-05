code=input('Code:').strip()
if len(code) != 5:
    print('false')
else:
    if code.isdecimal():
        print('true')
    else:
        print('false')