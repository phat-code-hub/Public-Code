def Area(info):
    height,width=info.split(',')
    return float(height)*float(width)
apartA=input("A:")
apartB=input("B:")
print("Apartment A" if Area(apartA)>=Area(apartB) else 'Apartment B')