n,m = map(int,input().split())

dp = {0:1,1:1}
def factorial(n):
    if n not in dp.keys():
        dp[n] = n * factorial(n-1)
    return dp[n]

ans = factorial(n) // factorial(n-m) // factorial(m)
print(ans)

# a = n - m if n - m > m else m
# b = n - m if n - m < m else m
# ans = 1
# for i in range(n,a,-1):
#     ans *= i

# ans = ans // factorial(b)
# print(ans)

