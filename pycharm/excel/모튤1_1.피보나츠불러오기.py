

# from Packages import fibo #경로 대소구분한다.
# fibo.fib(100)
# new_fib = fibo.fib
# new_fib(200)

# import Packages.fibo
#경로 대소구분한다. 이런인 경우 Packages.fibo로 바꾸어 야한다.
# Packages.fibo.fib(100)
# new_fib = Packages.fibo.fib
# new_fib(200)

from Packages import * #경로 대소구분한다. 경로의 패키지를 다 불러온다.

# 경로 대소구분한다. 간단하게 대신 함수바꾸어 줘야한다.
# 단축키 : Ctrl+Shift+화살표로 왔다갔다 할 수 있다.
from Packages.fibo import fib as f1, fib2 as f2
f1(100)
new_fib = f2
new_fib(200)



