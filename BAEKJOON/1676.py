n = int(input())

result = 1
for i in range(1,n+1):
    result *= i

cnt = 0
s = str(result)
for i in range(len(s)-1,-1,-1):
    if s[i] != '0':
        print(cnt)
        break
    else:
        cnt += 1

