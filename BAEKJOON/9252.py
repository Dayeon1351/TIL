import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
len_s1 = len(s1)
len_s2 = len(s2)

longest = []
dp = [""] * len_s1
for i in range(len_s2):
    temp = []
    for j in range(len_s1):
        if len(temp) < len(dp[j]):
            temp = dp[j]
        elif s1[j] == s2[i]:
            dp[j] = temp + [s1[j]]
        
        if len(longest) < len(dp[j]):
            longest = dp[j]

print(len(longest))
if longest:
    print("".join(longest))
