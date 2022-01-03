num = int(input())
max_val = 1000000007

dp = {0:0,1:1,2:1}
def fibo(n):
    if n in dp.keys():
        return dp[n]

    if n % 2 == 0:
        dp[n//2 + 1] = fibo(n//2 + 1) % max_val
        dp[n//2 - 1] = fibo(n//2 - 1) % max_val
        return dp[n//2 + 1] ** 2 - dp[n//2 -1] ** 2
    else:
        dp[n//2 + 1] = fibo(n//2 + 1) % max_val
        dp[n//2] = fibo(n//2) % max_val
        return dp[n//2 + 1] ** 2 + dp[n//2] ** 2
    
print(fibo(num)%max_val)