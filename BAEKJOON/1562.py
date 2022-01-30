from collections import defaultdict
max_val = 10 ** 9
n = int(input())
dp = [[defaultdict(int) for _ in range(10)]for _ in range(n+1)]

for i in range(1,10):
    dp[1][i][1<<i] = 1

for i in range(2,n+1):
    for k,v in dp[i-1][1].items():
        dp[i][0][k | 1 << 0] += v
    
    for j in range(1,9):
        for k,v in dp[i-1][j-1].items():
            dp[i][j][k | 1 << j] += v

        for k,v in dp[i-1][j+1].items():
            dp[i][j][k | 1 << j] += v
    

    for k,v in dp[i-1][8].items():
        dp[i][9][k | 1 << 9] += v

print(sum([dp[n][i][(1<<10)-1] for i in range(10)]) % max_val)