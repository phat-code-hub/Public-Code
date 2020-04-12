import math
INCHE_UNIT=12 #convert foot to inch
tape_surface_area=60*INCHE_UNIT+2
def Total_area(height,width):
    #calculate door area by inches and for both side of door
    return ((height*width)*INCHE_UNIT**2)
door_height=int(input('height: '))
door_width=int(input('width: '))
door_area=Total_area(door_height,door_width)
if door_area % tape_surface_area ==0 :
    tape_to_buy=math.floor(door_area//tape_surface_area)
else:
    tape_to_buy=math.floor(door_area//tape_surface_area)+1
print(tape_to_buy)