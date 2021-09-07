from collections import deque
n = int(input())
nums = deque([i for i in range(1,n+1)])

if len(nums) == 1:
    print(nums[0])
else: 
    while len(nums) > 1:
        nums.popleft()
        if len(nums) == 1:
            print(nums[0])
            break
        nums.append(nums.popleft())