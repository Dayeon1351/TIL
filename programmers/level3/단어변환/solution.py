from collections import deque

def isChange(len_word,cur_word,word):
    cnt = 0
    for a,b in zip(cur_word,word):
        if a == b:
            cnt += 1 
    
    return True if cnt == len_word - 1 else False

def solution(begin, target, words):
    answer = 0
    len_word = len(begin)
    queue = deque([begin])
    visited = {word : 0 for word in words}
    
    visited[begin] = 0
    while queue:
        cur_word = queue.popleft()
        if cur_word == target:
            answer = visited[target]
            break
            
        can_change = [word for word in words if isChange(len_word,cur_word,word) and visited[word] == 0]
        
        for adj_word in can_change:
            visited[adj_word] = visited[cur_word] + 1
            queue.append(adj_word)

    
    return answer
