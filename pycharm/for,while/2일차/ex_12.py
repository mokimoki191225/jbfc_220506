
#튜플형 변경할 수 없는 형

stat = ('별나', '봉호','성실','요온')

print(type(stat))
print('통계학과 \t:', stat)
print('통계학과[:2] \t:', stat[:2])
print('통계학과[-2:] \t:', stat[-2:])

# stat[2] = '영목'

stat = list(stat)
stat[2] = '영목'
print('통계 \t : ', stat)
stat = tuple(stat)
print('통계 \t : ', stat)
stat = set(stat)
print('통계 \t : ', stat)
stat = dict(stat)
print('통계 \t : ', stat)