
max_val = 1000000007
n = int(input())
dist = {}
dist[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]

def getCnt(d,cur,nxt):
    if d <= 1:
        return dist[d][cur][nxt]
    
    dist.setdefault(d,[[0 for _ in range(8)]for _ in range(8)])
    if dist[d][cur][nxt]:
        return dist[d][cur][nxt]
    
    half = d // 2
    other = half + 1 if d % 2 else half

    for k in range(8):
        dist[d][cur][nxt] += getCnt(half,cur,k) * getCnt(other,k,nxt)
        dist[d][cur][nxt] %= max_val

    return dist[d][cur][nxt]

print(getCnt(n,0,0))

