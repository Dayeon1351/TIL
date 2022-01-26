import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    visited[0] = True
    result = 0

    for i in range(1,n+1):
        if not visited[i]:
            idx = i
            loop = [idx]
            visited[idx] = True
            while 1:
                next_idx = arr[idx]
                if visited[next_idx]:
                    break
                idx = next_idx
                loop.append(idx)
                visited[idx] = True

            if loop and next_idx in loop:
                result += len(loop[loop.index(next_idx):])

    print(n-result)