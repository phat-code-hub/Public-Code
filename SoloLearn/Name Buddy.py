try:
    famous_person_names=input('Group Names: ').strip().split()
    myself=input('Your Name: ').strip()
    assert len(famous_person_names)>0 and len(myself)>0
    check_First_Letter=any([lambda n: n[0].upper()==myself[0].upper(),famous_person_names] )
    if check_First_Letter:
        print('Compare notes')
    else:
        print('No such luck')
except :
    print('Invalid Name!')

