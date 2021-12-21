# from itertools import product
# n,m = map(int,input().split())
# for i in list(product(range(1,n+1),repeat = m)):
#     print(' '.join(map(str,i)))

n,m = map(int,input().split())
num = [0] * m

def printNum(m,idx):
    if m == 0:
        print(" ".join(num))
    else:
        for i in range(1,n+1):
            num[idx] = str(i)
            printNum(m-1,idx+1)

printNum(m,0)
