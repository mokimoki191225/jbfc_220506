'''
def intel(cpu,ram,sdd):
    rate=cpu*ram*sdd
    return rate

cpu=100
ram=50
sdd=50

a=intel(cpu,ram,sdd)

print(a)
'''

# def intel(start,end):
#     for x in end:
#         result=0
#         x += result
#         print(result)
#
# b=intel(1,10)

# print(b)

# 짝수 입력하면 끝
def hol(a):
    while True:
        print("다시 넣어주세요")
        if a%2==0:
         print("짝수 끝")
        else:
            continue
    return a

i=int(input('숫자 골라봐'))
hol(i)
