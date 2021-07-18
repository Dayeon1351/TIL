from functools import reduce
def solution(clothes):
    answer = 0
    cnt = {}
    for i in clothes:
        kind = i[1]
        if kind not in cnt:
            cnt[kind] = 1
        else:
            cnt[kind] += 1
    

    if len(cnt.values()) == 1:
        answer = list(cnt.values())[0]
    else:   
        nums = list(cnt.values())
        answer = reduce(lambda x,y : x*(y+1),nums,1)-1
        
        
            
            
    return answer
