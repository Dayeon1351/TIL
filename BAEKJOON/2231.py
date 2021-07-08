def calculate(num):
    if num == 0:
        return 0
    else:
        return num%10 + calculate(num//10)

n = int(input())

for i in range(0,n+1):
    result = i + calculate(i)
    if result == n:
        print(i)
        break
else:
    print(0)
