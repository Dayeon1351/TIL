from collections import defaultdict

def find_network(dic,start):
    visited = []
    stack = [start]
    
    while stack:
        cur_node = stack.pop()
        visited.append(cur_node)
        for adj_node in dic[cur_node]:
            if adj_node not in visited:
                stack.append(adj_node)
                
    return visited

def solution(n, computers):
    answer = 0
    dic = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                dic[i] += [j]
    
    # print(dic)
    
    networks = list(dic.keys())
    
    while networks:
        start = networks.pop(0)
        visited = find_network(dic,start)
        networks = list(set(networks)-set(visited))
        answer += 1
    
    return answer
