from itertools import combinations
n,m = map(int,input().split())
for i in list(combinations(range(1,n+1),m)):
    print(' '.join(map(str,i)))