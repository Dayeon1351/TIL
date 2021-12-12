n = int(input())
m = int(input())
s = input()

ans = 0
idx = 1
cnt = 0
while idx < m - 1:
    if s[idx-1] == "I" and s[idx] == "O" and s[idx+1] == "I":
        cnt += 1
        if cnt == n:
            cnt -= 1
            ans += 1
        idx += 1
    else:
        cnt = 0
    idx += 1

print(ans)
