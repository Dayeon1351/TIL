import sys
input = sys.stdin.readline

mod = 1000000007

def multiply(a,b):
    if b == 0:
        return 1
    n = multiply(a,b//2)
    if b % 2 == 0:
        return n ** 2 % mod
    else:
        return n ** 2 * a % mod


factorial = [1] * 4000001
for i in range(2,4000001):
    factorial[i] = (factorial[i-1] * i) % mod

m = int(input())
for _ in range(m):
    n,k = map(int,input().split())
    
    num = (factorial[k] * factorial[n-k]) % mod
    num = multiply(num,mod-2)
    print((factorial[n] * num) % mod)