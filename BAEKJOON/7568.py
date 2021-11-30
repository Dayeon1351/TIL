n = int(input())
people = [list(map(int,input().split()))for i in range(n)]

rank = []
for i in range(len(people)):
    cnt = 1
    for j in range(len(people)):
        if i != j:
            x,y = people[i][0],people[j][0]
            p,q  = people[i][1],people[j][1]
            if x < y and p < q:
                cnt += 1
    
    rank.append(str(cnt))
print(" ".join(rank))
