import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

num = []
def printNum(m,idx):
    if m == 0:
        print(" ".join(num))
    else:
        flag = 0
        for i in range(idx,n):
            if flag != arr[i]:
                num.append(str(arr[i]))
                flag = arr[i]
                printNum(m-1,i)
                num.pop()

printNum(m,0)