import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

num = []
def printNum(m):
    if m == 0:
        print(" ".join(num))
    else:
        flag = 0
        for i in range(n):
            if flag != arr[i]:
                num.append(str(arr[i]))
                flag = arr[i]
                printNum(m-1)
                num.pop()

printNum(m)