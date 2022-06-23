
'''
묵지빠 게임
1. 게임시작 출력
2. 가위, 바위, 보를 하여 공격/수비를 결정
3. 공격 or 수비 묵, 찌, 빠?
4. 게임의 승부 or 공격/수비를 결정?
5. 결과메시지를 보여준다
cf 컴퓨터는 랜덤값, 플레이어는
'''

from random import randint



class GameMZP:

# 0.변수 설정하기

    computer  = int()
    computer2 = str()
    result    = str()
    user      = str()

# 1.수식 작성하기

    def com_ran(self): #컴퓨터 0=주먹,1=가위,2=보 출력
        self.computer = randint(0, 2)
        if self.computer == 0:
            computer2 = '가위'
        elif self.computer == 1:
            computer2 = '바위'
        else:
            computer2 = '보'
        return computer2
        print(computer2)

    def my_out(self): #나의 가위,바위,보 입력 로직, 유효성검증
        self.user = input('가위 바위 보 ? ')
        if self.user!='가위' and self.user!='바위' and self.user !='보':
           print('가위, 바위, 보 중에 입력바랍니다.')
        else:
            return self.user
        # print(self.user)

    def game(self): # 가위바위보 게임함수

        while self.computer != self.user:
            if self.computer == '가위' and self.user == '보':
                self.result = '컴퓨터 승리'
            elif self.computer == '바위' and self.user == '가위':
                self.result = '컴퓨터 승리'
            elif self.computer == '보' and self.user == '주먹':
                self.result = '컴퓨터 승리'
            else:
                self.result = '유저승리'
                break
            continue
            return result
        print(self.result)

com_output  =   GameMZP()

com_output.com_ran()
com_output.my_out()
# com_output.game()


#     #가위바위보 승부 로직
#     def games(self, computer, user):
#         if computer == 0:
#            computer = '가위'
#         elif computer == 1:
#             computer = '바위'
#         else:
#             computer = '보'
#
#     if computer == user:
#     result = '비겼다 !'
#     result2 = 'A'
# elif (computer == '가위' and user == '보') or (computer == '바위' and user == '가위') or (
# computer == '보' and user == '바위'):
# result = '컴퓨터 승리'
# result2 = 'B'
# else:
# result = '사용자 승리'
# result2 = 'C'
#
# print('컴퓨터: ', computer)
# print('사용자: ', user)
# print(result)
# return result2
# # 묵찌빠 승부 로직
# def win (computer , user , flag):
#
# while computer != user:
# if result2 = 'B' & result2 = 'A'
# print('컴퓨터 승리')
# elif result2 = 'C' & result2 = 'A'
# print('유저 승리')
# break
# elif result2 = 'C'
# while computer != user:
# break
# print('유저 승리')
# else:
# continue
#
#
#
#
# # 묵찌빠 승부 로직
# def mzpGames(self, computer, user, result2):
# if computer == 0:
# computer = '가위'
# elif computer == 1:
# computer = '바위'
# else:
# computer = '보'
#
# if computer == user:
# result = '끝났다!'
# result2 = '%s 승리', %result2
# elif (computer == '가위' and user == '보') or (computer == '바위' and user == '가위') or (
# computer == '보' and user == '바위'):
# result = '컴퓨터 승리'
# result2 = 'B'
#
# else:
# result = '사용자 승리'
# result2 = 'C'
#
# print('컴퓨터: ', computer)
# print('사용자: ', user)
# print(result)
# return result2
# def GO(self,result2):
# if result2 == 'B':
# print('나는 수비')
# elif result2 == 'A':
# print('비김')
# else:
# print('나는 공격')
# gameMZP = GameMZP()
# # gameMZP.GO()
# # gameMZP.bogame()
#
# while True:
# computer = gameMZP.ran()
# user = gameMZP.bogame()
# result = gameMZP.games(computer, user)
# if result != 'A':
# break
# else:
# pass