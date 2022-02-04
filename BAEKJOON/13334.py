import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = [sorted(list(map(int,input().split()))) for _ in range(n)]
d = int(input())

arr.sort(key= lambda x: x[1])

heap = []
result = 0
for a,b in arr:
    flag = b - d
    if a >= flag:
        heapq.heappush(heap,a)
    while heap and heap[0] < flag:
        heapq.heappop(heap)
    
    result = max(result,len(heap))

print(result)