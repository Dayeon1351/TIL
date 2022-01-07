import sys
input = sys.stdin.readline

n,m = map(int,input().split())
known = list(map(int,input().split()))[1:]
party = [list(map(int,input().split()))[1:]for i in range(m)] 

visited_party = [False] * m
visited_person = [False] * n
while known:
    num_known = known.pop()
    people = set()
    for i in range(m):
        if num_known in party[i]:
            people = people.union(party[i])
            visited_party[i] = True
        
    for p in people:
        if not visited_person[p-1]:
            known.append(p)
            visited_person[p-1] = True
            

print(visited_party.count(False))
