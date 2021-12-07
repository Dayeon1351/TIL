from collections import defaultdict

n = int(input())
memo = {1:1,2:3,3:5}

for i in range(4,n+1):
    memo[i] = (memo[i-1] + memo[i-2] * 2) % 10007

print(memo[n])