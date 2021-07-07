def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if i+1 > citations[i]:
            answer = i
            break
        elif len(citations) <= citations[len(citations)-1]:
            answer = len(citations)
            break
    
    return answer
