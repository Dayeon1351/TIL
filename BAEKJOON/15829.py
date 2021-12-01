import string
n = int(input())
line = input()
idx = list(string.ascii_lowercase)

result = 0
for i in range(n):
    result += (idx.index(line[i]) + 1) * (31**i)

ans = result % 1234567891
print(ans)