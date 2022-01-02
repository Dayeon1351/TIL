n = int(input())

cnt = 0
idx = 1
total = 0
while total<=n:
    total += idx
    cnt += 1
    idx += 1
print(cnt-1)