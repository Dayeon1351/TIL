import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split()))for i in range(n)]

cnt = [0,0]
def check_same_color(arr,cnt,x,y,idx):
    flag = arr[x][y]
    for i in range(x,x+idx):
        for j in range(y,y+idx):
            if flag != arr[i][j]:
                break
        else:
            continue
        break
    else:
        cnt[flag] += 1
        return 0

    num = idx // 2
    for i in range(x,x+idx,num):
        for j in range(y,y+idx,num):
            check_same_color(arr,cnt,i,j,num)
        
check_same_color(arr,cnt,0,0,n)
for c in cnt:
    print(c)