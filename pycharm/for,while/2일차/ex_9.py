
# 리스트 슬라이싱
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
print('\n무지개색깔 \t\t :', rainbow)

result = rainbow[2:5]
print('rainbow[2:5]\t\t:', result)

result = rainbow[:3]
print('rainbow[ :3] :', result)

result = rainbow[:]
print('rainbow[ : ] :', result)

result = rainbow[::2] #건너뛰고 두번째것
print('rainbow[::2] :', result)

result = rainbow[::3] #건너뛰고 세번째것
print('rainbow[::3] :', result)

result = rainbow[::4] #건너뛰고 세번째것
print('rainbow[::4] :', result)

result = rainbow[::5] #찍고 다섯번째
print('rainbow[::5] :', result)

result = rainbow[-3:]
print('rainbow[-3:] :', result)

result = rainbow[::-1]  #역순
print('rainbow[::-1]:', result)