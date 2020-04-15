try:
    num_str= input('Four digits number: ')
    assert len(num_str)==4
    test_num_str=num_str
    before_result=int(test_num_str)
    after_result=0
    while True:
        desc_num=int(''.join(sorted(str(before_result),reverse=True)))
        asc_num=int(''.join(sorted(str(before_result))))
        after_result=desc_num-asc_num
        if after_result == before_result:
            break
        else:
            before_result=after_result

except :
    print('Invalid Number')

