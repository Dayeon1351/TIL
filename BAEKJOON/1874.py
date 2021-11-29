import sys
n = int(sys.stdin.readline())

stack = []
oper = []
cnt = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        stack.append(cnt)
        oper.append('+')
        cnt += 1
        
    if stack[-1] == num:
        stack.pop()
        oper.append('-')
    else:
        print('NO')
        break
else:
    for i in oper:
        print(i)
        