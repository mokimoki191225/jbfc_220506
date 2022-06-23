
year=int(input('몇년?'))

is_leap = (year%400==0)or(year%100!=0)and(year%4==0)

if is_leap:
    print('윤년')
else:
    print('윤년아닙니다')


