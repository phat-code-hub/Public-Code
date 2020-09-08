import re
reg=re.compile(r'^(\w)+://(w{3}.)?youtu[.be|be.com][/(\w)+|/(\w)+?=(\w)+]')
#linkstr= input('Link: ').strip()
linkstr='https://www.youtube.com/watch?v=kbx365'
linkstr='https://youtu.be/kbx365'
if len(linkstr) >0:
    m=reg.search(linkstr)
    if m:
        links=m.group()
        print(links)
    else:
        print('Not Found')
else:
    print('Nothing')