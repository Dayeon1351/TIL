import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int,input().split()))

def solution():
    min_val = float('INF')
    a,b,c = 0,0,0
    for i in range(n-2):
        flag = arr[i]
        start,end = i+1,n-1
        while start < end:
            num = flag + arr[start] + arr[end]

            if min_val >= abs(num):
                min_val = abs(num)
                a,b,c = flag,arr[start],arr[end]
            
            if num < 0:
                start += 1
            elif num > 0:
                end -= 1
            else:
                break

    print(a,b,c)

solution()