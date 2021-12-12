import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for i in range(n)]

def quadTree(size,x,y):
    if size == 1:
        return arr[x][y]
    
    else:
        result = []
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j] != arr[x][y]:
                    result.append('(')
                    result.extend(quadTree(size//2,x,y))
                    result.extend(quadTree(size//2,x,y+size//2))
                    result.extend(quadTree(size//2,x+size//2,y))
                    result.extend(quadTree(size//2,x+size//2,y+size//2))
                    result.append(')')
                    return result
        else:
            return arr[x][y]


print("".join(quadTree(n,0,0)))