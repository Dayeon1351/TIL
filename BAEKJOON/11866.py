n,k = map(int,input().split())
people = [i for i in range(1,n+1)]

idx = 0
cnt = 1
out = []
while people:
    if cnt % k == 0:
        out.append(str(people.pop(idx)))
        idx -= 1

    cnt += 1
    idx += 1
    
    if idx == len(people):
        idx = 0

ans = "<" + ", ".join(out) + ">"
print(ans)