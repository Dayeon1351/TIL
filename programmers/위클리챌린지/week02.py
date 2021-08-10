from collections import Counter
def solution(scores):
    answer = ''
    scores = list(map(list,zip(*scores)))
    avgs = []
    
    for score in scores:
        idx = scores.index(score)
        m,n = max(score),min(score)
        mCnt,nCnt = score.count(m), score.count(n)
        
        # if Counter(score)[score[idx]] == 1 and (m == score[idx] or n == score[idx]):
        if (m == score[idx] and mCnt == 1) or (n == score[idx] and nCnt == 1):
            score.pop(idx)
            
        avgs.append(sum(score)//len(score))
            
    for avg in avgs:
        if avg >= 90:
            answer += "A"
        elif avg >= 80:
            answer += "B"
        elif avg >= 70:
            answer += "C"
        elif avg >= 50:
            answer += "D"
        else:
            answer += "F"
            
    return answer
