from itertools import product
n,m = map(int,input().split())
for i in list(product(range(1,n+1),repeat = m)):
    print(' '.join(map(str,i)))