import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

num = []
visited = [False] * n
def printNum(m,idx):
    if m == 0:
        print(" ".join(num))
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i] = True
                num.append(str(arr[i]))
                printNum(m-1,i)
                num.pop()
                visited[i] = False

printNum(m,0)
