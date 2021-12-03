import sys
k,n = map(int,input().split())
lines = [int(sys.stdin.readline()) for i in range(k)]

left = 1
right = max(sum(lines) // n, min(lines))
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for line in lines:
        cnt += line // mid
    
    if cnt >= n:
        left = mid + 1
        
    else:
        right = mid - 1
            
print(right)