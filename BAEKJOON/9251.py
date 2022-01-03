import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
len_s1 = len(s1)
len_s2 = len(s2)

dp = [0] * len_s1

for i in range(len_s2):
    cnt = 0
    for j in range(len_s1):
        if cnt < dp[j]:
            cnt = dp[j]
        elif s1[j] == s2[i]:
            dp[j] = cnt + 1 

print(max(dp))