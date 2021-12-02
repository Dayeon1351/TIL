# 1 7 19 37 61
# 6 12 18 24
n = int(input())
cnt = 1
num = 1
while 1:
    if n <= num:
        break
    num += 6 * cnt
    cnt += 1
print(cnt)