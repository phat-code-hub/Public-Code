import sys
JP_moneys=[5000,1000,500,100,50,10,5,1]
paper_num=[]
def calc_Changes(total):
    changeTotal=total
    for money in JP_moneys:
        paper=changeTotal // money
        changeTotal=changeTotal- paper*money
        paper_num.append(paper)
    changes=dict(zip(JP_moneys,paper_num))
    print('おつりは {} 円 で：'.format(total))
    for k in changes.keys():
        name='コイン'
        unit='個'
        if changes[k]>0:
            if k >500:
                name='紙幣'
                unit='枚'
            print('{0} {1} : {2} {3}'.format(name,k,changes[k],unit))
insert_note_str=input('inserted money: ').strip()
item_price_str=input('product price: ').strip()
if (not insert_note_str.isdecimal) or (not item_price_str.isdecimal):
    print('正しい整数値を入力してください')
    sys.exit()
else:
    change=int(insert_note_str)-int(item_price_str)
    if change > 0:
        calc_Changes(change)
    else:
        print('投入金額が不足しています')
        sys.exit()