import sys
input = sys.stdin.readline

n,b = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

def matrix_mul(x,y):
    result = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k] * y[k][j]
            
            result[i][j] %= 1000
    
    return result

def divide(b,matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return matrix_mul(matrix,matrix)
    else:
        m = divide(b//2,matrix)
        if b % 2 == 0:
            return matrix_mul(m,m)
        else:
            return matrix_mul(matrix_mul(m,m),matrix)
    
    

result = divide(b,arr)
for row in result:
    for col in row:
        print(col%1000,end=' ')
    print()
