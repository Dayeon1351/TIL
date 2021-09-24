import sys
def calculateNum(n):
    if n < 3:
        return n
    elif n == 3:
        return 4
    else:
        return calculateNum(n-1) + calculateNum(n-2) + calculateNum(n-3)

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    print(calculateNum(n))