import math
#Define Clas point Coordinate
class Point:
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
    #Define distance between two Points 
    def distance(self,coord):
        coordX= (self.x-coord.x)**2
        coordY=(self.y-coord.y)**2
        root=math.sqrt(coordX+coordY)
        #separate fractional and integer parts of root
        d,i=math.modf(root)
        if d==0:
            return int(root)
        else:
            return round(math.sqrt(coordX+coordY),2)
#----------------------------------------------
# Extract x and Y values from input Points' infomation
def take_Points(data):
    coords=data.split()
    point1=coords[0]
    point2=coords[1]
    #Remove ()and divide x and Y Point
    point1=point1.replace('(','').replace(')','').split(',')
    point2=point2.replace('(','').replace(')','').split(',')
    return float(point1[0]),float(point1[1]),float(point2[0]),float(point2[1])
#----------------------------------------------
# main code 
info=input('Points: ').strip() 
X1,Y1,X2,Y2=take_Points(info)
Point1= Point(X1,Y1)
Point2= Point(X2,Y2)
print(Point1.distance(Point2))