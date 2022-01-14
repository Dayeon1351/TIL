import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
len_s1 = len(s1)
len_s2 = len(s2)

dp = [0] * len_s1
arr = [[] for _ in range(len_s1)]
for i in range(len_s2):
    cnt = 0
    temp = ""
    for j in range(len_s1):
        if cnt < dp[j]:
            cnt = dp[j]
            temp = "".join(arr[j])
        elif s1[j] == s2[i]:
            dp[j] = cnt + 1
            arr[j] = temp+s1[j]
            
idx = dp.index(max(dp))
print(dp[idx])
if dp[idx] != 0:
    print(arr[idx])
