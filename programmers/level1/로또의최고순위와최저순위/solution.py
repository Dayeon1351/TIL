def solution(lottos, win_nums):
    answer = []
    intersect = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    answer.append(rank[intersect+zero])
    answer.append(rank[intersect])
    
    
    return answer
