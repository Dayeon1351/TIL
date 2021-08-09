from collections import Counter
def solution(scores):
    answer = ''
    scores = list(zip(*scores))
    avgs = []
    
    for score in scores:
        idx = scores.index(score)
        m = max(score)
        n = min(score)
        mCnt = score.count(m)
        nCnt = score.count(n)
        if (m == score[idx] and mCnt == 1) or (n == score[idx] and nCnt == 1):
        # if Counter(score)[score[idx]] == 1 and (m == score[idx] or n == score[idx]):
            avgs.append((sum(score) - score[idx]) // (len(score) - 1))
        else:
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
