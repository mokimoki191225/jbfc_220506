
#리팩토링 -> 함수를 계속 개선하다.

def add(a,b):
    result = a+b
    return result

result = add(10,20)
print(result)

def add2(a,b,c=0):
    result = a+b+c
    return result

result = add2(10,20,30)
print(result)

def add3(nums):
    result = 0
    for num in nums:
        result+=num
    return result

result = add3([10,20,30])
print(result)

def add4(*nums):
    result=0
    for num in nums:
        result+=num
    return result

result = add4(10,20,30)
print(result)

def add5(nums):
    result=1
    for num in nums:
        result*=num
    return result

result = add5([10,20,30]) #10x10x20x30
print(result)

def add6(nums):
    result = 20
    for num in nums:
        result+=num
    return result

result = add6([10,20,30]) #10x10x20x30
print(result)

# bmi 함수

def bmi(b,c):
    a=c/((b/100)**2)
    return float(a)

b=input('키')
b=int(b)

c=input('몸무게')
c=int(c)

d=bmi(b,c)
print(d)

if d>= 23 and d< 25 :
    BMI_result = "과체중"
elif d>= 25 and d< 30:
    BMI_result = "비만"
elif d>= 30:
    BMI_result = "고도비만"
else:
    BMI_result = "정상"

print(BMI_result)