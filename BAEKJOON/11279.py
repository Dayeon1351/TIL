import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    num = int(input())
    if num == 0:
        result = 0 if not heap else -heapq.heappop(heap)
        print(result)
    else:
        heapq.heappush(heap,-num)
