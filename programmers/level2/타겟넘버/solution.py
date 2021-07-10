def findTarget(nums,val,target,idx):
    result = 0
    if idx == len(nums):
        result = 1 if val == target else 0
    else:
        n = nums[idx]
        result += findTarget(nums,val+n,target,idx+1)
        result += findTarget(nums,val-n,target,idx+1)
        
    return result

def solution(numbers, target):
    answer = 0
    answer = findTarget(numbers,0,target,0)
    return answer
