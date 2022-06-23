
#윤년만들기

year = int(input('몇년?'))
is_leap=False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap=True
        else:
            is_leap=False
    else:
        is_leap = True
else:
    is_leap = False #tap키와 Sfit+tap

if is_leap:
    print('윤년')
else:
    print('윤년아닙니다')


