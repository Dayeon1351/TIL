def findNum(val,target,num):
    result = 0
    if val == target:
        result = 1
    elif val > target or num > target:
        result = 0
    else:
        val+=num
        result = findNum(val,target,num+1)
    return result   
    
def solution(n):
    answer = 0
    for i in range(1,n+1):
        answer+=findNum(i,n,i+1)
        # result  = 0
        # j = i
        # while result < n:
        #     result+=j
        #     j+=1
        # if result == n:
        #     answer+=1
        
    return answer
