n = int(input())

cnt = n // 5
ans = 0

if n % 5 == 4:
    ans = cnt - 1 + 3 if cnt >= 1 else -1
elif n % 5 == 3:
    ans = cnt + 1
elif n % 5 == 2:
    ans = cnt - 2 + 4 if cnt >= 2 else -1
elif n % 5 == 1:
    ans = cnt - 1 + 2
else:
    ans = cnt

print(ans)