from itertools import combinations_with_replacement
n,m = map(int,input().split())

for i in list(combinations_with_replacement(range(1,n+1),m)):
    print(' '.join(map(str,i)))