import heapq
def solution(n, works):
    answer = 0
    nums = []     # max heap에 대한 리스트
    
    # max heap 생성
    for w in works:
        heapq.heappush(nums,(-w,w))   # (우선순위,값)

    while n > 0:
        maxNum = heapq.heappop(nums)                      # 가장 큰 값 반환
        heapq.heappush(nums,(maxNum[0]+1,maxNum[1]-1))    # maxNum[0] :우선순위 maxNum[1] : 값  => 내림차순 순서 유지(값기준)
        n-=1  

    for num in nums:
        answer += num[1]**2 if num[1] > 0 else 0
                
    return answer
