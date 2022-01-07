from math import gcd
import sys
input = sys.stdin.readline


max_val = 1000000007
def multi(x,y):
    if y == 1:
        return x
    if y % 2 != 0:
        return x * multi(x,y-1) % max_val
    t = multi(x,y//2)
    return t * t % max_val


answer = 0
m = int(input())

for i in range(m):
    a,b = map(int,input().split())

    k = gcd(a,b)
    a //= k
    b //= k

    answer += b * multi(a,max_val-2) % max_val
    answer %= max_val

print(answer)
