class A:
    __var=5
    def pr(self):
        print(self.__var)
class B(A):
    __var=4
B().pr() # 5