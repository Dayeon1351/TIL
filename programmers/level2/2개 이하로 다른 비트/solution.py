# 하나씩 비교하는 것은 효율적이지 못함 => 시간초과
# def findNum(n):
#   i = 1
#   while format(n^(n+i),'b').count('1') > 2:
#     i+=1
#   return n+i


def findNum(n):
    result = 0
    
    # n이 짝수인 경우 이진수 표현 시 마지막이 0 이기 때문에 1을 더해준 값이 조건에 해당된다.
    if n % 2 == 0:
        result = n + 1
    else:
        nums = list(format(n,'b'))
        if '0' not in nums:    
            nums.insert(0,'1')
            nums[1] = '0'
        else:
            idx = nums[::-1].index('0')
            nums[-(idx+1)] = '1'
            nums[-idx] = '0'
        
        result = int("".join(nums),2)
    
    return result
  
        
def solution(numbers):
    answer = [findNum(n) for n in numbers]
    return answer
