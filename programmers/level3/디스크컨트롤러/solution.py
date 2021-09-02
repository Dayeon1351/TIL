import heapq

def add_job(jobs,heap,cur_idx):
    while jobs and jobs[0][0] < cur_idx:
        point,time = jobs.pop(0)
        heapq.heappush(heap,(time,point))

    return heap


def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x :(x[0],x[1]))
    length = len(jobs)
    heap = []
    cur_idx = 0
    
    while jobs:
        point,time = jobs.pop(0)
        cur_idx = point + time
        answer += cur_idx - point
        
        heap = add_job(jobs,heap,cur_idx)

        while heap:
            time,point = heapq.heappop(heap)
            cur_idx += time
            answer += cur_idx - point
            heap = add_job(jobs,heap,cur_idx)
    
    answer = answer // length          
    
    return answer
