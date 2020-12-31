def ispal(s):
    try:
        w=[c for c in s]
        w.reverse()
        p="".join(w)
        if p==s:
            return True
        else:
            return False
    except:
        return False
# print(ispal("rotator"))
print(ispal(34543))