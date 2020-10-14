def get_book_upper(index):
    items=['book','notebook','sketchbook']
    try:
        book=str(items[index])
    except (IndexError,TypeError) as e:
        print(f"例外発生しました：{e}")
    else:
        return book.upper()
print(get_book_upper(2))
print(get_book_upper(4))