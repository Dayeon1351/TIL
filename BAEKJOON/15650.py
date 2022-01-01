# from itertools import combinations
# n,m = map(int,input().split())
# for i in list(combinations(range(1,n+1),m)):
#     print(' '.join(map(str,i)))

n,m = map(int,input().split())
num = []
visited = [False] * n

def printNum(m,idx):
    if m == 0:
        print(" ".join(num))
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i] = True
                num.append(str(i+1))    
                printNum(m-1,i)
                num.pop()
                visited[i] = False

printNum(m,0)
