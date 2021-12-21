a,b,c = map(int,input().split())

def getResult(a,b):
    if b == 0:
        return 1
    n = getResult(a,b//2)
    if b % 2 == 0:
        return n ** 2 % c
    else:
        return n ** 2 * a % c

print(getResult(a,b)%c)
