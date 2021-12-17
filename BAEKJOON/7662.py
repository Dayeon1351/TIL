import sys,heapq
input = sys.stdin.readline

t = int(input())
for i in range(t):
    k = int(input())
    
    max_heap = []
    min_heap = []
    visited = [0] * (k+1)

    for j in range(k):
        oper,n = input().split()
        if oper == 'I':
            heapq.heappush(min_heap,[int(n),j])
            heapq.heappush(max_heap,[-int(n),j])
            visited[j] = 1
        else:
            if n == '1':
                while max_heap and visited[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    while max_heap and visited[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)        
    
    while min_heap and visited[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")
        