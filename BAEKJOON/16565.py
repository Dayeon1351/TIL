from math import factorial

mod = 10007
n = int(input())

def comb(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

dp = [[0] * 14 for _ in range(n+1)]

dp[0][0] = 1
for i in range(n):
    for j in range(13):
        for k in range(4):
            if i+k <= n:
                dp[i+k][j+1] += dp[i][j] * comb(4,k)

idx = 1
result = 0
while 4 * idx <= n:
    result += comb(13,idx) * dp[n-(4*idx)][13-idx]
    result %= mod
    idx += 1

print(result % mod)
