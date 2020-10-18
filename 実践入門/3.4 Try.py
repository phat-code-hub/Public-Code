def get_book(index):
    items=['note','notebook','sketchbook']
    try:
        return items[index]
    except(IndexError,TypeError) as e:
        print(f'例外発生しました：{e}')
        return '範囲外'

get_book(3)
get_book('3')