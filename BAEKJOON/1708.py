import sys
input = sys.stdin.readline

def ccw(a,b,c):
    v = (b[0]-a[0],b[1]-a[1])
    u = (c[0]-b[0],c[1]-b[1])
    
    if v[0] * u[1] > v[1] * u[0]:
        return True
    
    return False

def convex_hull(point):
    stack = []
    for p in point:
        while len(stack) >= 2:
            fir,sec = stack[-2],stack[-1]
            if ccw(fir,sec,p):
                break
            stack.pop()
        stack.append(p)

    return len(stack)

n = int(input())
point = [list(map(int,input().split())) for _ in range(n)]
point.sort()

result = -2
result += convex_hull(point)

point.reverse()
result += convex_hull(point)

print(result)