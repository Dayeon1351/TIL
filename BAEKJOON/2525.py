h,m = map(int,input().split())
time = int(input())

if m+time >= 60:
    h+=(m+time)//60
    m=(m+time)%60
else:
    m+=time
if h > 23:
    h-=24

print(h,m)
