# map_str=input('Nhap mang:').strip()
# maps=map_str.upper().split(',')
maps='xPxxx,xxPPx,xxxxx,xxxPx,xxxxx'.upper().split(',')
countP=0
step=0
rows=[]
cols=[]
for r in range(len(maps)):
    if 'P' in maps[r]:
        #Check 'P' in same row or not
        countP=maps[r].count('P') 
        if countP>1: # in the same row
            for y in range(len(maps[r])):
                if maps[r][y]=='P':           
                    rows.append(r)
                    cols.append(y)
        else: # difference row
            rows.append(r)
            cols.append(maps[r].index('P'))
#Calculate step      
row_step=abs(rows[0]-rows[-1])
col_step=abs(cols[0]-cols[-1])
step=col_step+row_step
print(step)