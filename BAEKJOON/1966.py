t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    paper = list(map(int,input().split()))
    
    cnt = 1
    while 1:
        if m == 0 and paper[0] == max(paper):
            print(cnt)
            break
        else:
            if paper[0] == max(paper):
                paper.pop(0)
                m -= 1
                cnt += 1
            else:
                paper.append(paper.pop(0))
                m  = m - 1 if m > 0 else len(paper) -1