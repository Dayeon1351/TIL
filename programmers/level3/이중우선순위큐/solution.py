import heapq
def solution(operations):
    answer = []
    nums = []
    
    for operation in operations:
        oper,n =operation.split()     
        
        if oper == 'I':
            heapq.heappush(nums,int(n))       #최소힙 생성
        else:
            if nums:
                if n == "1":
                    nums.remove(max(nums))
                else:
                    heapq.heappop(nums)
        
        
    answer = [0,0] if not nums else [max(nums),min(nums)] 
        
    return answer
