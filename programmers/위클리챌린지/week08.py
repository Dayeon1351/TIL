def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        sizes[i][0],sizes[i][1] = max(sizes[i]),min(sizes[i])
    
    
    size = list(map(list,zip(*sizes)))
    
    w = max(size[0])
    h = max(size[1])
    
    answer = w*h
        
    return answer
