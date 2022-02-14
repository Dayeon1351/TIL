import sys
input = sys.stdin.readline

mod = 1000000007
n = int(input())
arr = sorted(list(map(int,input().split())))

result = 0
p = 1
for i in range(n):
    result = (result + p * (arr[i]-arr[n-i-1])) % mod
    p = (p * 2) % mod

print(result)