class System:
    def __init__(self,x):
        self.x=x
    class out:
        def println(self,other):
            print(other)
try:
    System.out.println("OK")
except:
    print("No")