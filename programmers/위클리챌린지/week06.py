def solution(weights, head2head):
    answer = []
    win = []
    for i in head2head:
        win.append(0 if i.count('W') == 0 else i.count('W') / (i.count('W')+i.count('L')))
    
    heavy = []
    for i in range(len(head2head)):
        idx = [j for j in range(len(head2head[i])) if head2head[i][j] == "W"]
        heavy.append(len([weights[k] for k in idx if weights[i] < weights[k]]))
    
    order = [-i for i in range(1,len(weights)+1)]
    
    player = list(map(list,zip(win,heavy,weights,order)))
    
    player.sort(reverse = True)
    
    for p in player:
        answer.append(-p[3])
    
    return answer
