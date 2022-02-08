import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = 0
for _ in range(n):
    num = int(input())

    while stack and stack[-1][0] < num:
        result += stack.pop()[1]

    if stack and stack[-1][0] == num:
        cnt = stack.pop()[1]
        result += cnt
        if stack:
            result += 1
        stack.append((num,cnt+1))
    
    else:
        if stack:
            result += 1
        stack.append((num,1))
    
    
print(result)