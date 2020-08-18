def get_book(index):
    items=['note','notebook','sketchbook']
    try:
        return items[index]
    except  (IndexError,TypeError) as e:
        print('例外発生しました。{e}'.format(e=e))
        return '範囲外です。'
        raise
print(get_book('1'))