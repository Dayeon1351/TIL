# from itertools import combinations_with_replacement
# n,m = map(int,input().split())

# for i in list(combinations_with_replacement(range(1,n+1),m)):
#     print(' '.join(map(str,i)))

n,m = map(int,input().split())
num = []

def printNum(m,idx):
    if m == 0:
        print(" ".join(num))
    else:
        for i in range(idx,n):
            num.append(str(i+1))    
            printNum(m-1,i)
            num.pop()    

printNum(m,0)
