import sys
from collections import deque

t = int(input())
for i in range(t):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    
    nums = deque(sys.stdin.readline().strip()[1:-1].split(","))
    
    idx = 0
    for j in p:
        if j == 'R':
            idx = 0 if idx == -1 else -1
        else:
            if not nums or n == 0:
                print("error")
                break
            
            if idx == 0:
                nums.popleft()
            else:
                nums.pop()
            
    else:  
        if idx == -1:
            nums.reverse()
                  
        print("["+ ",".join(nums) + "]")