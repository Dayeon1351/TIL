# n : 자리수
# s : 합
def solution(n, s):
    answer = []     
    
    if n > s:
        answer = [-1]
    else:
        while n > 0:
            p = s//n
            answer.append(p)
            s-=p
            n-=1
            
    return answer
