class Number:
    def __init__(self,num):
        self.value=num
    @property
    def isEven(self):
        if self.value % 2 == 0:
            return True
        else:
            return False
x=Number(int(input()))
print(x.isEven)
