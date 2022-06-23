
year=int(input('몇년?'))

is_leap=False
if year %400==0:
    is_leap=True
elif year % 100==0:
    is_leap=False
elif year % 4==0:
    is_leap=True
else:
    is_leap=False

if is_leap:
    print('윤년')
else:
    print('윤년아닙니다')
