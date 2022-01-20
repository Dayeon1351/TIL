import sys
input = sys.stdin.readline

n = int(input())
arr = tuple(map(int,input().split()))

start,end = 0,n-1
min_val = float('INF')
s,e = 0,0
while start < end:
    num = arr[start]+arr[end]

    if min_val >= abs(num):
        min_val = abs(num)
        s,e = arr[start],arr[end]
    
    if num < 0:
        start += 1
    elif num > 0:
        end -= 1
    else:
        break

print(s,e)