boxes=[]
msg='Trash'
for i in range(4):
    boxes.append(input('nhap: ').strip().upper())
for box in boxes:
    rev_box=box[::-1]
    if box == rev_box:
        msg='Open'
        break
print(msg)