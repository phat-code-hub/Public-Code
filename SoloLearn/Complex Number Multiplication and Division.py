#Examine two complex numbers A(a1+a2j) and B(b1+b2j):
#A*B= (a1+a2j)(b1+b2j)=a1*b1 + a1*b2*j + a2*b1*j + a2*b2*j*j
#    =(a1*b1-a2*b2) +(a1*b2+a2*b1)j   (note : j^2=-1)
#A/B = A* (1/B)=(a1+a2j)/(b1+b2j)=(a1+a2j)(b1-b2j) /(b1+b2j)(b1-b2j)
#    =(a1*b1-a1*b2j+a2j*b1-a2j*b2j)/(b1^2-b2^2*j^2)
#    =[(a1*b1+a2*b2)-(a1*b2-a2*b1)j]/(b1^2+b2^2)
# => real_part of A/B : (a1*b1+a2*b2)/(b1^2+b2^2)
#    imaginary_part of A/B : -(a1*b2-a2*b1)/(b1^2+b2^2)
#Note : This Code uses float number to calulate division 
#------------------------------------------------------------------
class complx():
    def __init__(self,real,img):
        self.real=real
        self.img=img
    #Multiple define
    def mul(self,other):
        real_part=self.real*other.real - self.img*other.img
        img_part=self.real*other.img+self.img*other.real
        return complx(real_part,img_part)
    #Division define
    def div(self,other):
        deno=other.real**2+other.img**2
        real_part=(self.real*other.real+self.img*other.img)/deno
        img_part=(-1)*(self.real*other.img-self.img*other.real)/deno
        return complx(real_part,img_part)
#------------------------------------------------------------------
def display(result):
    LIMIT=5
    print('{real}, {img}'.format(real=round(result.real,LIMIT),img=round(result.img,LIMIT)))
#------------------------------------------------------------------
try:
    nums=input('four numbers:').strip().split(',')
    A =complx(float(nums[0]),float(nums[1]))
    B =complx(float(nums[2]),float(nums[3]))
    C=complx.mul(A,B)
    D=complx.div(A,B)
    E=complx.div(B,A)
    display(C)
    display(D)
    display(E)
except :
    print('Invalid')
