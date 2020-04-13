def isalphanum(c):
    return '0' <=c <='9' or 'A' <=c <="Z" or 'a'<=c<='z'
def isdot(c):
    return c=='.'
def isatmark(c):
    return c=='@'
def isend(c):
    return c=='$'
def isEMail(str):
    str+='$'
    INIT=0;
    LOCAL_NOTDOT=1
    LOCAL_DOT=2
    ATMART=3
    DOMAIN_NOTDOT=4
    DOMAIN_DOT=5
    OK=6
    NG=7
    state=INIT
    return state ==OK
#------------------------------------
#Main Code
if __name__=='__main__':
    content=input('文字列→')
    if isEMail(content):
        print("メールアドレス")
    else:
        print('メールアドレスではありません')
