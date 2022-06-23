
signal_color = ''

while signal_color != 'blue' and signal_color != 'red':
    signal_color=input('색을 영문으로 입력 (blue/red) :')

    if signal_color=='blue':
        print('신호등은 파란색입니다. 길을 건너세요!!')
    elif signal_color=='red':
        print('신호등은 빨간색입니다. 기다리세용')
    else:
        print('잘못된 색입니다. 다시 입력해용')

print('프로그램을 종료!!')
# print('종료'), tap키 누르면 바깥으로 나온다