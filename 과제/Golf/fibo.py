
#피보나치 수열

def fib(n):
    a,b = 0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()

def fib2(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

print(fib(3))
print(fib2(3))