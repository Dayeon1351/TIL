from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)       # 내림차순 정랼
    
    deq = deque(people)
    
    while deq:
        m = deq.popleft()     # 가장 큰 값 
        if len(deq) > 0 and m + deq[-1] <= limit:   # 가장 큰 값과 가장 작은 값의 합이 limit 보다 작을 경우
            deq.pop()
        answer+=1

    return answer
