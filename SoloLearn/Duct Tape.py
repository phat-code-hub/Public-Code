import math
INCHE_UNIT=12 #foot<-> inch
tape_surface_area=60*2/INCHE_UNIT #convert to feet
def Total_area(height,width):
    #calculate door area by inches and for both side of door
    return height*width
door_height=int(input('height: '))
door_width=int(input('width: '))
door_area=Total_area(door_height,door_width)
# for 2 side of door
if door_area % tape_surface_area ==0 :
    tape_to_buy=door_area//tape_surface_area*2
else:
    tape_to_buy=(math.floor(door_area//tape_surface_area)+1)*2 
print(tape_to_buy)