#Examine two complex numbers A(a1+a2j) and B(b1+b2j):
#A*B= (a1+a2j)(b1+b2j)=a1*b1 + a1*b2*j + a2*b1*j + a2*b2*j*j
#    =(a1*b1-a2*b2) +(a1*b2+a2*b1)j   (note : j^2=-1)
#A/B = A* (1/B)=(a1+a2j)/(b1+b2j)=(a1+a2j)(b1-b2j) /(b1+b2j)(b1-b2j)
#    =(a1*b1-a1*b2j+a2j*b1-a2j*b2j)/(b1^2-b2^2*j^2)
#    =[(a1*b1+a2*b2)-(a1*b2-a2*b1)j]/(b1^2+b2^2)
# => real_part of A/B : (a1*b1+a2*b2)/(b1^2+b2^2)
#    imagine_part of A/B : -(a1*b2-a2*b1)/(b1^2+b2^2)
class complx():
    def __init__(self,real,img):
        self.real=float(real)
        self.img=float(img)
    def mul(self,other):
        real_part=self.real*other.real - self.img*other.img
        img_part=self.real*other.img+self.img*other.real
        return complx(real_part,img_part)
    def div(self,other):
        deno=other.real**2+other.img**2
        real_part=float((self.real*other.real+self.img*other.img))
        img_part=self.real*other.img-self.img*other*real
        return complx(real_part,img_part)
A=complx(1,2)
B=complx(3,4)
C=complx.mul(A,B)
D=complx.div(B,A)
print('{real}, {img}'.format(real=C.real,img=C.img))
print('{real}, {img}'.format(real=D.real,img=D.img))