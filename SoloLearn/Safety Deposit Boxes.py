LIMIT_TIME=5
items_list=input('Items List :').strip()
specific_item=input('find item ').strip()
items=items_list.split(',')
found_box_order=items.index(specific_item)+1
print(found_box_order*LIMIT_TIME)