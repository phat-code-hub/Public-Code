def has_book(items):
    copied=items.copy()
    while copied:
        item= copied.pop()
        if 'book' in item:
            print("Found!")
            break
    else:
        print("Not Found!") 
has_book(['note'])
has_book(['book'])
has_book(['note', 'notebook'])     

